#!/usr/bin/perl
# vim:ts=2 expandtab ai tw=125 nu sw=2
use strict ;
use warnings ;

=pod

When a customer installs the new formmail he will first get the option of

a) - Simple

Using a template to generate a single contact page.  No Perl knowledge is required.
In addition a customised help page will be generated which will tell the customer
how to link to the contact page from the page(s) of his website.  The customer
will need the ability to write an html link on one or more of his web site pages.

or b) - Expert

using the original system (recommended only for those comfortable with coding in
PERL).  This will have all the options available for multiple pages and multiple
recipients.

Security.

In both cases the contact page will only be valid from the domain of the installed
code and the address of the recipient is hidden from the user, ie the email address
of 'us' in contact us is hidden.  It is also hidden from email mining search robots.

Whichever option is chosen the script that generates the contact us page for option
a) self destructs This is to stop a site visitor from running the script at another
time and changing the recipient address.

=cut

print <<"END";
Content-Type: text/html; charset=utf8

<html>
  <head>
    <title>FormMail Installation</title>
  </head>
  <body style="width: 600px;">
    <h1>Formmail Installation Options</h1>
    <p>You have two options at this point.
    <ul>
      <li>If you want just a single contact page <br />
        choose the <strong>&quot;simple&quot;</strong>  option (recommended).<br />
        No Perl knowledge is required.  A contact page will be generated and also 
        a customised help page  that will tell you how to
        access the contact page from the page(s) of your website.
        <form  id='formA' action="simple.cgi" method="post">
          <input value="Simple" type="submit" name='show_form' />
        </form>
      </li>

      <li>or if you are comfortable with coding in Perl<br />
        and you want multiple and different contact pages <br />
        and/or you want multiple recipients<br />
        choose the <strong>&quot;expert&quot;</strong> option<br />

        <form  id='formB' action="index.cgi" method="post">
          <input value="Expert" type="submit" />
        </form>
      </li>
    </ul>
    </p>
  </body>
</html>
END
unlink $0 ;
