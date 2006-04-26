%define		_xfce_ver 4.3.90.1
Summary:	Port of Xfce engine to GTK+-2.0
Summary(pl):	Port silnika Xfce do GTK+-2.0
Name:		gtk-xfce-engine
Version:	2.3.90.1
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.xfce.org/archive/xfce-%{_xfce_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	f3ac06faff7ed1c1fbb701eeb56a6c1a
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 1:2.6.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	gtk+2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of Xfce engine to GTK+-2.0.

%description -l pl
Port silnika Xfce do GTK+-2.0.

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
