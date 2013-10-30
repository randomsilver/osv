#!/usr/bin/perl
use strict;
use warnings;
use Authen::Captcha;

# You MUST create the following directories yourself. FormMail will not work
# without them, unless you are not using Captcha support.

# Set this to a directory that is not accessible via the web.
# Often something like /home/yourname/.captcha_data
my $captcha_datadir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/.captcha_data";

# Set this to a directory that will store the captcha images. This should
# be accessible via the web because it will be included on the page.
# Often something like /home/yourname/public_html/fm/captcha_img
my $captcha_outputdir = "/websites/123reg/LinuxPackage23/on/es/il/onesilveredvein.com/public_html/contact/img";

# This should be the same as the directory above, but using the web accessible
# URL path. If you have /home/yourname/public_html/fm/captcha_img above then
# you will need /fm/captcha_img here.
my $image_dir = "/contact/img";


# Use the following few settings to configure the form values.

# This should be the location of the FormMail.cgi script.
my $formmail = "/contact/FormMail.cgi";

# This is where you want the email to go.
my $recipient = 'info@onesilveredvein.com';

# This is where the user should be taken to after submitting the form.
my $redirect = "http://onesilveredvein.com";


my $captcha = Authen::Captcha->new(
  data_folder => $captcha_datadir,
  output_folder => $captcha_outputdir,
  );

my ($md5sum, $chars) = $captcha->generate_code(4);
# eliminate ambiguous chars from $chars
my $bad_chars = 1;
while ($bad_chars) {
    if ( $chars =~ m/o|0|O|l|i|1|q|9|6|b|s|S|5|2|Z/) {
        ($md5sum, $chars) = $captcha->generate_code(4);
    } else {
        $bad_chars = 0;
    }
}


# Modify the HTML below to make your form how you like it.
# Ensure that you read the instructions carefully.
# Do not edit outside the comment sections, unless you are sure
# you know what you're doing.
print <<"END";
Content-Type: text/html; charset=ISO-8859-1

<html>
  <head>
    <title>FormMail Instructions</title>
    <link href="/css/bootstrap.css" rel="stylesheet" media="screen">
    <link href="/css/bootstrap-responsive.css" rel="stylesheet" media="screen">
    <link href="/css/styles.css" rel="stylesheet" media="screen">
  </head>
  <body>
    <form action="$formmail" method="post">
      <table>
        <tr>
          <td>
            <input type="hidden" name="subject" value="This is a test" />

            <!-- This section must remain the same for Captcha support. -->
            <input type="hidden" name="recipient" value="$recipient" />
            <input type="hidden" name="redirect" value="$redirect" />
            <input type="hidden" name="captcha-md5sum" value="$md5sum" />
            <label>Email Address: </label>
          </td><td>
            <input type="text" size="20" name="email">
          </td>
        </tr><tr>
          <td>
            <label>Name: </label>
          </td><td>
            <input type="text" size="20" name="realname">
          </td>
        </tr>
        <!-- End section -->

        <!-- You can add extra form items here -->
          <td style="vertical-align: top;">
            <label>Message: </label>
          </td><td>
            <textarea name="message" style="height: 120px; width: 300px;"></textarea>
          </td>
        </tr><tr>

        <!-- The following section must stay here for Captcha support. -->
          <td colspan="2">Please enter the image verification code below.</td>
        </tr><tr>
          <td><img src="$image_dir/$md5sum.png" /></td>
          <td>
            <input type="text" size="20" name="captcha-text" id="captcha-text" />
          </td>
        </tr>
        <!-- End section -->

        <tr>
          <td>&nbsp;</td>
          <td>&nbsp;</td>
        </tr>

        <tr>
          <td>
            <input value="Submit Comments" type="submit" />
          </td><td>
            <input value="Clear Form" type="reset" />
          </td>
        </tr>
      </table>
    </form>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.10.1/jquery.js"></script>
    <script src="http://code.jquery.com/jquery-migrate-git.min.js"></script>
    <script src="/js/bootstrap/bootstrap.min.js"></script>
    <script src="/js/bootstrap/bootbox.min.js"></script>
    <script src="/js/bootstrap/jquery.quicksand.js"></script> 
    <script src="/js/custom-2.js"></script>
  </body>
</html>
END
