#
%define		_snap 20040813

Summary:	Port of XFce engine to GTK+-2.0
Summary(pl):	Port silnika XFce do GTK+-2.0
Name:		gtk-xfce-engine
Version:	2.2.0
Release:	0.%{_snap}.1
License:	GPL
Group:		Themes/Gtk
Source0:	http://ep09.pld-linux.org/~havner/xfce4/%{name}-%{_snap}.tar.bz2
# Source0-md5:	c368e832a3408945669b324b9e6de6ec
URL:		http://www.xfce.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xft-devel
Requires:	gtk+2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of XFce engine to GTK+-2.0.

%description -l pl
Port silnika XFce do GTK+-2.0.

%prep
%setup -q -n %{name}-2

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

# no *.la for gtk engines
rm -f $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%{_datadir}/themes/Xfce*
