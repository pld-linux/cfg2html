Summary:	Tool to collect Linux system configuration into a HTML and text file
Name:		cfg2html
Version:	2.50
Release:	1
License:	Unknown
Group:		Applications/System
URL:		http://www.cfg2html.com/
Source0:	http://www.cfg2html.com/%{name}-linux-%{version}-20120601_all.zip
# Source0-md5:	a3d2991a515f5ed5f23ea0b7dda8f82c
BuildRequires:	unzip
Obsoletes:	cfg2html-linux < 2.50-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config to HTML is the "swiss army knife" for the ASE, CE, sysadmin
etc. It helps to get the nessary informations to plan an update, to
performe basic trouble shooting or performance analysis.

As a bonus cfg2html creates a nice HTML and plain ASCII documentation
from Linux System, Cron and At, installed Hardware, installed
Software, Filesystems, Dump- and Swapconfiguration, LVM, Network
Settings, Kernel, Systemenhancements and Applications, Subsystems.

%prep
%setup -qc

mv %{name}-linux_*.changes Changes
mv descript.ion README

%{__tar} xzf %{name}-linux_%{version}*.tar.gz
mv %{name}-linux-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo '.so man8/cfg2html-linux.8' > $RPM_BUILD_ROOT%{_mandir}/man8/cfg2html.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* AUTHORS contrib collect *.html *.txt
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/files
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/plugins
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/systeminfo
%attr(755,root,root) %{_bindir}/cfg2html
%attr(755,root,root) %{_bindir}/cfg2html-linux
%{_mandir}/man8/cfg2html.8*
%{_mandir}/man8/cfg2html-linux.8*
