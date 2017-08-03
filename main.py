#/usr/bin/env python
#coding: utf-8

'''
Author: yanpqi@gmail.com
Description: 使模板可以用python来生成
TODO:
  - 添加更多的选择项，可以让用户更从容地自定义证书.
  - 添加更多的证书模板
Refernce:
  - http://www.ruanyifeng.com/blog/2011/05/how_to_choose_free_software_licenses.html
  - http://www.gnu.org/licenses/license-list.html
'''

import os
import sys
import datetime
import re

RE_PROJECT = re.compile('\{\{\s+project\s+\}\}', re.M)
RE_ORG = re.compile('\{\{\s+organization\s+\}\}', re.M)
RE_YEAR = re.compile('\{\{\s+year\s+\}\}', re.M)

def collect_license():
    licenses = []
    for f in os.listdir('templates'):
        licenses.append(f.split('.')[0])
    return licenses

def output_license(license):
    proj = ''
    while len(project_name) <= 0:
        proj = raw_input('请输入项目名称: ')
    org = ''
    while len(organize) <= 0:
        org = raw_input('请输入组织名称: ')

    content = ''
    with open('templates/%s.txt' %license, 'r') as f:
        content = f.read()

    if len(content) > 0:
        print type(RE_PROJECT)
        print proj
        (content, number) = re.subn(RE_PROJECT, proj, content)
        (content, number) = re.subn(RE_ORG, org, content)
        (content, number) = re.subn(RE_YEAR, str(datetime.datetime.now().year), content)

    with open('LICENSE', 'w') as f:
        f.write(content)
        print 'LICENSE has generated, please move to your project'

def main(argvNone):
    licenses = collect_license()
    print '目前支持如下证书：' + str(licenses)
    license = raw_input('请选择证书名称, 不清楚直接回车')
    if len(license) > 0 and license in licenses:
        output_license(license)
        return
    else:
        select = raw_input('修改后可否闭源(y/N)? ')
        if select == 'y':
            select = raw_input('修改的文件是否要添加版权声明(y/N)? ')
            if select == 'y':
                license = apache
            else:
                select = raw_input('软件可否使用你的名义宣传(y/N)? ')
                license = mit if select == 'y' else bsd
        else:
            select = raw_input('新代码必须使用本许可证(y/N)? ')
            if select == 'y':
                license = gpl
            else:
                select = raw_input('修改处是否要提供说明(y/N)? ')
                license = mozilla if select == 'y' else lgpl
        output_license(license)
    
if __name__ == '__main__':
    sys.exit(main(sys.argv))

