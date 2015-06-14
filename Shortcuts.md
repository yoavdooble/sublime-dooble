 SJS: 
 Server functions:
 
$sj   - Convert object to JSON
$sgg  - Get Global variable (userid, username, siteid, etc...)
$ssg  - Set Global variable (mainly used for sending emails)
$ssc  - Set Cookie variable into the user's browser.
$sgc  - Get Cookie variable.
$sss  - Set Session variable.
$sgs  - Get Session variable
$sq   - get a Query String from the current url address.
$sp   - get a Parameter that was sent to the current module.
$sf   - Get the Form that was sent (via HTTP POST)
$ssm  - Send Mail to the given address.
$sa   - create a new Action. the db variable stores all the data that was sent into the action.
$sba  - set an action to occurre Before the given Action.  the db variable stores all the data that was sent into the action.
$saa  - set an action to occurre After the given Action.  the db variable stores all the data that was sent into the action.
$surl - Get the current Url. set to false if you want the url without the domain name.
$sdyc - Decrypt a Value.
$senc - Encrypt a Value.
$sr   - Redirect the user to a new url.

 Service Functions:

$sget   - send a HTTP Get request.
$spost  - send a HTTP Post request.
$sexist - checks if a Site Exists.

 Util Functions:

$uqs - Sets a value to the Query String on the given url
$req - adds an sjs that is requierd to the code. prevents from adding multiple unnecessary import statements.

 Data functions:
 
$dq  - performs a Data Query request. will return a variable with only one field (the first, by default) of the first row found. uses auto-joins.
$dqr - performs a Data Query Row request. Will return an object all the fields of the first row found. uses auto-joins.
$dql - performs a Data Query List request. will return a list containing all the fields of all the rows it will find.
$ds  - performs a SQL SELECT query. will return a variable with only one field (the first, by default) of the first row found.
$dsu - performs a SQL UPDATE query.
$dsd - performs a SQL DELETE query. IT HAS TO HAVE A WHERE STATMENT.
$dsu - performs a SQL INSERT query.
$dsr - performs a SQL SELECT query. will return an object conatining all the fields of the first row found.
$dsl - performs a SQL SELECT query. will return a list of object containing all the field of the rows that were found.
$dc  - will return all the Data that is used by the Current module.
$dcl - will return all the Data that is used by  the Current module as a List.
$de - will make the variable safe to use in queries by Escaping the data.

 Miscellaneous SJS:
 
$site - will create a variable containing all the Site Details.
$tms  - will Throw a text msg.
$tsj  - will Throw an object as a JSON
$cb   - will create a Comment Block JS (can b used in any SJS block of '.js' File).

 HTML Functions:
 
@bb     - will open a SJS Block in an html file.
@bil    - will open a SJS block In-Line.
@form   - will create a Form block area.
@con    - creates a Config statemnet.
@if     - creates an If statemnt to use in html.
@ifelse - creates an If statment, with an Else block in the html.
@loop - creates a loop that itirate over the given parameters.
@isjs   - Imports a SJS. the src can be modified if the file is out of the SJS default folder.
@icss   - Imports a CSS. the src can be modified if the file is out of the CSS default folder (styles).
@ijs    - Imports a JS. the src can be modified if the file is out of the JS default folder.
@rc     - will return the Row Count of the current module.
@rn     - will return the Row Number of the current module. to be used inside an item file.
@gd     - Get the current Date.
@block - dds a text Block.

 Form Elements:

@uitext        - creates an UI element to contain Text.
@uitextarea    - creates an UI element to contain TextArea.
@uicheck       - creates an UI element to contain Check Box.
@uicomboselect - creates an UI element to contain ComboBox. the data will come from a sql table.
@uicombovalue  - creates an UI element to contain ComboBox. the data will come from the given hard-coded values.
@uidate        - creates an UI element to contain DatePicker. the default format is yyyy/MM/dd
@uisubmit      - creates an UI element to contain Submit. the default 'save' action will save the given fields to the current module Table.
@uihidden     - creates an UI element to contain Hidden element.

Miscellaneous HTML/JS:

@deb - will pop up the browser debugger Debugger. will only work on Front-End '.js' files.
@cl  - will write the given value into the Console Log. doesn't work on SJS files that are used by ajax or services.
@cb  - will create a SJS Comment Block  on a HTML file. this comment will not be visible to the user.

 Common Forms:
 
#apiform - creates an API Form.
#handler - will create an Handler as a js object.
#sql     - will create a SQL Builder. to be used for complex sql queries.
                
