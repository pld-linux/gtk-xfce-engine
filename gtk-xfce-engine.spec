%define		_xfce_ver 4.1.99.1
Summary:	Port of XFce engine to GTK+-2.0
Summary(pl):	Port silnika XFce do GTK+-2.0
Name:		gtk-xfce-engine
Version:	2.2.2
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{_xfce_ver}/%{name}-%{version}.tar.gz
# Source0-md5:	32cca81be97ccc1199f62cec1422de78
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	gtk+2 >= 1:2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of XFce engine to GTK+-2.0.

%description -l pl
Port silnika XFce do GTK+-2.0.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no *.la for gtk engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%{_datadir}/themes/Xfce*
