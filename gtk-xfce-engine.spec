#
%define		xfce_version 4.8.0
#
Summary:	Xfce theme engine for GTK+
Summary(pl.UTF-8):	Motyw Xfce dla GTK+
Name:		gtk-xfce-engine
Version:	2.8.0
Release:	1
License:	GPL
Group:		Themes/GTK+
Source0:	http://archive.xfce.org/src/xfce/gtk-xfce-engine/2.8/%{name}-%{version}.tar.bz2
# Source0-md5:	195f4dc2e6632143ca9ca6bd17ca4680
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.8
BuildRequires:	glib2-devel >= 1:2.18.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.8.0
Requires:	gtk+2 >= 2:2.14.0
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
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# no *.la for gtk engines
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-2.0/2.*/engines/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/2.*/engines/*.so
%{_datadir}/themes/Xfce*
