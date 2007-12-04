#
%define		xfce_version 4.4.2
#
Summary:	Xfce theme engine for GTK+
Summary(pl.UTF-8):	Motyw Xfce dla GTK+
Name:		gtk-xfce-engine
Version:	2.4.2
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://www.xfce.org/archive/xfce-%{xfce_version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	00eb6a62defe6867d28a18569b96d151
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.10.6
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
Requires:	gtk+2 >= 2:2.10.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xfce theme engine for GTK+.

%description -l pl.UTF-8
Motyw Xfce dla GTK+.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%{_datadir}/themes/Xfce*
