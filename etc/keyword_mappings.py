# Imports
import os
import sys
runPath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(runPath, ".."))


vuln_types = {

	'DoS' : {
		'denial of service',
		'dos',
	},

	'Code Execution' : {
		'(code|expression|statement) execution',
		'execute ([a-zA-Z]+ *){0,3}[ ]{0,}(expression(s){0,1}|statement(s){0,1}|code)',
	},

	'Overflow' : {
		'(buffer|integer) overflow',
	},

	'Memory Corruption' : {
		'memory corruption',
	},

	'SQLi' : {
		'sqli',
		'(sql|database|db) injection',
	},

	'XSS' : {
		'xss',
		'cross[\- ]{0,}site scripting',
		'(js|javascript) injection',
	},

	'Directory Traversal' : {
		'(path|directory) traversal',
		'(access|read) file[- ]{0,1}system',
	},

	'HTTP Response Splitting' : {
		'(http){0,1}[ ]{0,1}response splitting',
	},

	'Bypass Something' : {
		'spoof(ing){0,1}',
	},

	'Gain Information' : {
		'(obtain|gain|collect|get|read|download)[ ]{0,3}(sensitive|critical|arbitrary){0,1}[ ]{0,3}(information|data|file[s]{0,1}|source(s|[ ]code))',
		'(eavesdrop(ping){0,1}|sniff(ing){0,1})',
	},

	'Gain Privileges' : {
		'(gain|obtain|elevat(e|ion){0,1})[ ]{0,1}(of){0,1}[ ]{0,1}privilege(s){0,1}',
	},

	'CSRF' : {
		'csrf',
		'(cross[\- ]{0,1}site){0,1} request forgery',
	},

	'Broken Authentication' : {
		'broken authentication',
	},

	'Sensitive Data Exposure' : {
		'data exposure',
	},

	'Broken Authentication' : {
		'xml external entities',
		'xxe',
	},

	'Broken Access Control' : {
		'broken access control',
	},

	'Security Misconfiguration' : {
		'security misconfiguration',
	},

	'Insecure Deserialization' : {
		'insecure deserialization',
	},

	'Insufficient Logging & Monitoring' : {
		'insufficient (logging|monitoring)',
	},

}
