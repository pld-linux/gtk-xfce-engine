%define		_xfce_ver  4.0.5
Summary:	Port of XFce engine to GTK+-2.0
Summary(pl):	Port silnika XFce do GTK+-2.0
Name:		gtk-xfce-engine
Version:	2.1.9
Release:	1
License:	GPL
Group:		Themes/Gtk
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{_xfce_ver}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{_xfce_ver}/src/%{name}-%{version}.tar.gz
# Source0-md5:	f2a057cb840777684102cf127b38f40b
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.4.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xft-devel
Requires:	gtk+2 >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of XFce engine to GTK+-2.0.

%description -l pl
Port silnika XFce do GTK+-2.0.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/engines/libxfce \
	$RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.0/engines/libxfce.so

# no *.la for gtk engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.4.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/2.4.*/engines/*.so
%{_datadir}/themes/Xfce*
