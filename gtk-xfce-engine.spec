Summary: 	Port of xfce engine to GTK+-2.0
Name: 		gtk-xfce-engine
Version: 	2.1.1
Release: 	0.1
License:	GPL
URL: 		http://www.xfce.org/
Source0: 	http://belnet.dl.sourceforge.net/sourceforge/xfce/%{name}-%{version}.tar.gz
# Source0-md5:	71fe40468c67f7d3828694be4a8710aa
Group: 		Themes/Gtk
Requires:	gtk+2 >= 2.0.0
BuildRequires: 	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	fontconfig-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of Xfce engine to GTK+-2.0.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.*/engines/*.so
%{_libdir}/gtk-2.0/2.2.*/engines/*.la
%{_datadir}/*
