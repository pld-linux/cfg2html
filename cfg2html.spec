Summary:	Tool to collect Linux system configuration into a HTML and text file
Name:		cfg2html
Version:	2.86
Release:	2
License:	Unknown
Group:		Applications/System
Source0:	http://www.cfg2html.com/%{name}-linux-%{version}-20140319_all.zip
# Source0-md5:	ccd0b66c05e51dab3d7a7eb4b760fd59
URL:		http://www.cfg2html.com/
BuildRequires:	unzip
Obsoletes:	cfg2html-linux < 2.50-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Config to HTML is the "swiss army knife" for the ASE, CE, sysadmin
etc. It helps to get the nessary information to plan an update, to
perform basic troubleshooting or performance analysis.

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
