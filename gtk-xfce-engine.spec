Summary:	Port of Xfce engine to GTK+-2.0
Summary(pl):	Port silnika Xfce do GTK+-2.0
Name:		gtk-xfce-engine
Version:	2.1.4
Release:	1
License:	GPL
Group:		Themes/Gtk
Source0:	http://www.xfce.org/archive/xfce4-rc3/src/%{name}-%{version}.tar.gz
# Source0-md5:	7b0ead5c9fb6cb7e1558f3b08bcf2471
URL:		http://www.xfce.org/
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xft-devel
Requires:	gtk+2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of Xfce engine to GTK+-2.0.

%description -l pl
Port silnika Xfce do GTK+-2.0.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# no *.la for gtk engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.2.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/2.2.*/engines/*.so
%{_datadir}/themes/Xfce*
