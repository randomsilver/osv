#!/usr/bin/perl
# vim:ts=2 expandtab ai tw=125 nu sw=2

use strict ;
use CGI ;
use Data::Dumper ;
use Authen::Captcha ;

=pod

This will generate an executable perl script called fm-contact-us.cgi in this
directory The customer does not need to have any knowledge of Perl to use this.
He just customises a standard contact us form.

It also generates a help file which will explain how the customer can insert html
links from pages on his web site to the fm-contact-us.cgi script.  The behind
the scenes code ensures that links to the fm-contact-us.cgi script from other web
sites will not work.

After running once, this script deletes itself so that it cannot be used by a
visitor to this web site and overwrite the original customisation.

=cut

# The location of the FormMail.cgi script.
my $formmail = "/contact/FormMail.cgi" ;

# This directory is not accessible via the web.
my $captcha_datadir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/.captcha_data" ;

# This directory will store the captcha images.
my $captcha_outputdir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/contact/img" ;

# This is the same as the directory above, but using the web accessible
# URL path.
my $image_dir = "/contact/img" ;

# This is where the user should be taken to after submitting the form.
my $redirect = "http://onesilveredvein.com/contact/email_sent.html" ;

my $title ;
my $email ;
my $realname ;
my $recipient ;
my $invitation ;
my $cgi = new CGI ;
my $name ;
my $domain = 'onesilveredvein.com' ;

my $next_action = $cgi->param ( 'next_action' ) || '' ;
#warn "next_action is $next_action" ;

#warn "cgi parms " . Dumper ( $cgi->param () ) ;
if ( ( $next_action eq 'Change' ) || ( $next_action eq '' ) ) {
    #warn __LINE__ . " Editing form" ;

    # Edit form
    $title    = $cgi->param ( 'title' )    || 'Contact us' ;
    $email    = $cgi->param ( 'email' )    || '' ;
    $realname = $cgi->param ( 'realname' ) || '' ;
    $name     = $cgi->param ( 'name' )     || 'webmaster' ;

    print $cgi->header () ;
    print <<"END";
<!DOCTYPE html>
<html>
  <head>
    <title>FormMail Simple Customisation</title>
  </head>
  <body style="width: 600px;">
    <h1>Formmail Simple Customisation.</h1>

<p>With the information you provide here a simple 'contact us' form will be generated
   which can be used by visitors to your web site to contact you.</p>
 
    <p>Fill in the boxes - default values have been inserted but you may 
overwrite them as you wish.</p>
<form method='post'>

<h3>The form title</h3>
<p>What is to go at the top of your email area</p>
<input type='text' name='title' value='$title' />

<h3>Invitation</h3>
<p>Instructions to display to your visitors</p>
<textarea name='invitation' cols=64 rows=8 wrap=virtual>

Please enter your name, your email address, a subject, your
message, and the code for humans in the boxes and click send.
We apologise for asking you to enter a code but it blocks
those electronic robots from clogging up our mailbox with spam.

Thank you.
We shall get back to you as soon as possible.
</textarea>
<h3>Who is going to receive the email</h3>
<p>You must put a single valid email address here.  The format is <br />
name&#064;onesilveredvein.com.  Name should be only letters, numbers, '-', '_', or '.'.<br />
It is a security feature of Formmail that the recipient should be hosted from the same domain 
as the website.  <br />
The recipient email address is not displayed 
on the form presented to the visitor and is held in the code in a way which 
hides it from email address mining robots. 
</p>
<input type='text' name='name'   value='$name' />&#064;onesilveredvein.com
<p>
Click <input type='submit' name='next_action' value="Submit" > to generate a <em>$title</em> form.
</p>
</form>
END
} ## end if ( ( $next_action eq...))

# Show form
elsif ( $next_action eq 'Submit' ) {
    #warn __LINE__ . " Showing form" ;
    #warn "Show form ", Dumper ( $cgi->param () ) ;

    my $ok = 1 ;
    my $error ;

    # Check the values
    $title = $cgi->param ( 'title' ) || 'Contact us' ;
    $title =~ s/:/&#058;/g ;    # Replace any colon with its html entity
    $title =~ s/'/&#039;/g ;    # Replace any single quote with its html entity
    $title =~ s/"/&#034;/g ;    # Replace any double quote with its html entity
    $invitation = $cgi->param ( 'invitation' ) || 'Please fill in the boxes.  Thank you.' ;
    $invitation =~ s/:/&#058;/g ;    # Replace any colon with its html entity
    $invitation =~ s/'/&#039;/g ;    # Replace any single quote with its html entity
    $invitation =~ s/"/&#034;/g ;    # Replace any double quote with its html entity
    $name = $cgi->param ( 'name' ) || '' ;

    if ( $name ) {
        $name =~ s/^\s*// ;
        $name =~ s/\s*$// ;
        if ( $name =~ m/[^a-zA-Z0-9\-\._]/ ) {
            $error .= 'Invalid recipient name ' ;
            $ok = 0 ;
        }

    }
    else {
        $ok = 0 ;
        $error .= 'Please specify a recipient name ' ;
    }

    $recipient = $name . '@' . $domain ;

    my $captcha = Authen::Captcha->new (
                                         data_folder   => $captcha_datadir,
                                         output_folder => $captcha_outputdir,
                                       ) ;

    my ( $md5sum, $chars ) = $captcha->generate_code ( 4 ) ;

    # eliminate ambiguous chars from $chars
    my $bad_chars = 1 ;
    while ( $bad_chars ) {
        if ( $chars =~ m/o|0|O|l|i|1|q|9|6|b|s|S|5|2|Z/ ) {
            ( $md5sum, $chars ) = $captcha->generate_code ( 4 ) ;
        }
        else {
            $bad_chars = 0 ;
        }
    }
    print $cgi->header () ;
    print <<"END";

<!DOCTYPE html>
<html>
  <head>
    <title>FormMail Simple Contact Form</title>
  </head>
  <body style="width: 600px;">
    <h1>Formmail Simple Contact Form </h1>

<p>This what your form will look like
   which can be used by visitors to your web site to contact you.</p>
 
<form method='post'>

<hr>
<h3>$title</h3>
<p>$invitation</p>
<form method='post'>
<table>
<tr><td><label>Your Name </label></td><td><input type='text' name='realname' size=40></td></tr>
<tr><td><label>Your Email </label></td><td><input type='text' name='email' size=40></td></tr>
<tr><td><label>Subject </label></td><td><input type='text' name='subject' size=60></td></tr>
<tr><td><label>Your message </label></td><td><textarea name='message' cols=64 rows=8 wrap=virtual></textarea></td></tr>
        <!-- The following section displays a captcha request  -->
        <tr>
          <td><label>Enter the letters </label></td><td><img src="$image_dir/$md5sum.png" /> <input type="text" size="20"
          name="captcha-text" id="captcha-text" /></td>
        </tr>
        <!-- End section -->
<tr><td>&nbsp;</td><td align='center'> <button value='Send query'>Send query </button></td></tr>
</table>
<p> <p>
<hr>
END
    if ( $ok ) {
        print <<"END";
<p> If this is OK click 
<input type='submit' name='next_action' value='OK'>
to save your customised <em>contact us</em> form,
</p><p> else click 
<input type='submit' name='next_action' value='Change'>
to go back and change something.
</p>
<p>
The recipient will be <strong>$recipient</strong> but this is not shown on the form.
</p>
END
    }
    else {
        print <<"END";
<p><font color='#ff0000'> Error</br>
$error
</p><p> Click
<input type='submit' name='next_action' value='Change'>
to go back to make corrections
</p>
END
    }
    print <<"END";
<input type='hidden' name='title' value="$title" >
<input type='hidden' name='invitation' value="$invitation">
<input type='hidden' name='email' value="$email" >
<input type='hidden' name='recipient' value="$recipient" >
<input type='hidden' name='realname' value="$realname" >
<input type='hidden' name='redirect' value="$redirect" >
<input type='hidden' name='name' value="$name" >
</form> 
END
} ## end elsif ( $next_action eq 'Submit')

elsif ( $next_action eq 'OK' ) {

    #         # generate the form as specified by the user.
    $title     = $cgi->param ( 'title' ) ;
    $recipient = $cgi->param ( 'recipient' ) ;
    $recipient =~ s/@/\\@/ ;    # else dear old perl thinks it's an array symbol
    $invitation = $cgi->param ( 'invitation' ) ;
    $redirect ;
    $email ;
    $realname ;

    #warn "Title is $title" ;
    #warn "recipient is $recipient" ;

    # warn "invitation is $invitation" ;

    open CONTACT_US, " > fm-contact-us.cgi" or die "Can't create fm-contact-us.cgi ; $!" ;

    print CONTACT_US << "END_OF_CONTACT_US";
#!/usr/bin/perl
use strict;
use warnings;
use Authen::Captcha;
use CGI ;

my \$cgi = new CGI ;

# this directory is not accessible via the web.
my \$captcha_datadir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/.captcha_data";

# this directory will store the captcha images. This should
# be accessible via the web because it will be included on the page.
my \$captcha_outputdir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/contact/img";

# This directory is the same as above, but using the web accessible
# URL path.
my \$image_dir = "/contact/img";

# This should be the location of the FormMail.cgi script.
my \$formmail = "/contact/FormMail.cgi";

# This is where the user should be taken to after submitting the form.
my \$redirect = "http://onesilveredvein.com/contact/email_sent.html";


my \$captcha = Authen::Captcha->new(
  data_folder => \$captcha_datadir,
  output_folder => \$captcha_outputdir,
  );

my (\$md5sum, \$chars) = \$captcha->generate_code(4);
# eliminate ambiguous chars from \$chars
my \$bad_chars = 1;
while (\$bad_chars) {
    if ( \$chars =~ m/o|0|O|l|i|1|q|9|6|b|s|S|5|2|Z/) {
        (\$md5sum, \$chars) = \$captcha->generate_code(4);
    } else {
        \$bad_chars = 0;
    }
}
my \$title      = '$title' ;
my \$recipient  = '$recipient' ;
my \$invitation = '$invitation' ;
my \$email    ;
my \$realname  ;

print \$cgi->header () ;

print << "END_OF_HTML";

<!DOCTYPE html>
<html>
<head>
<title>$title</title>
</head>
<body>
<h1>$title</h1>
<p>$invitation</p>
<form  action="$formmail" method='post'>
<table>
<tr><td><label>Your Name </label></td><td><input type='text' name='realname' size=40></td></tr>
<tr><td><label>Your Email </label></td><td><input type='text' name='email' size=40></td></tr>
<tr><td><label>Subject </label></td><td><input type='text' name='subject' size=60></td></tr>
<tr><td><label>Your message </label></td><td><textarea name='message' cols=64 rows=8 wrap=virtual></textarea></td></tr>
        <!-- The following section displays a captcha request  -->
        <tr>
          <td><label>Enter the letters </label></td>
          <td><img src="$image_dir/\$md5sum.png" /> <input type="text" size="20" name="captcha-text" id="captcha-text" /><td></td>
        </tr>
        <!-- End section -->
<tr><td>&nbsp;</td><td aligh='center'> <button value='Send my email'>Send my email </button></td></tr>
</table>
<p> <p>
<input type='hidden' name='title' value="$title" >
<input type='hidden' name='recipient' value='$recipient' >
<input type='hidden' name='redirect' value="$redirect" >
<input type='hidden' name='captcha-md5sum' value="\$md5sum" >
</form>

</body></html>
END_OF_HTML
END_OF_CONTACT_US
    chmod( 0755, 'fm-contact-us.cgi' ) ;

    # Generate a help file
    open HELP_SIMPLE, "> help_simple_contact.html" or die "Can't create help_simple_contact.html; $!" ;
    print HELP_SIMPLE << "END_OF_HELP_SIMPLE";
<!DOCTYPE html>
<html>
<head>
<title>Help simple formmail</title>
</head>
<body>
<center>
<h1>Help for using the simple formmail option</h1>
<p>
To link to your <em>Contact Us</em> form  from any page on your website all you have to do is place the following HTML 
on that page.<br /><br />
&lt;a href=&quot;http://onesilveredvein.com/contact/fm-contact-us.cgi&quot;&gt;Contact us&lt;/a&gt;
</p>
<br />
<p>To test the <em>Contact Us</em> form  click on 
<a href="/contact/fm-contact-us.cgi">this link</a> and send yourself a message.
</p>
</center>
</body>
</html>
END_OF_HELP_SIMPLE
    close HELP_SIMPLE ;

    unlink $0 ;

    print $cgi->header () ;
    print <<"END";

<!DOCTYPE html>
<html>
  <head>
    <title>FormMail Simple Customisation Complete</title>
  </head>
  <body style="width: 600px;">
    <h1>Formmail Simple Customisation Complete</h1>
    <p>Your form is now in fm-contact-us.cgi in this directory.  <br />
    Click <a href='help_simple_contact.html' >help_simple_contact.html</a> 
    to see how to use this from a page on your web site.
    </p>
</body>
</html>
END
} ## end elsif ( $next_action eq 'OK')

