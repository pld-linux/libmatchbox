Summary:	Utility library used by Matchbox utilities
Summary(pl):	Biblioteka narzêdziowa u¿ywana przez narzêdzia Matchbox
Name:		libmatchbox
Version:	1.9
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://projects.o-hand.com/matchbox/sources/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9f73e7515cc4679171a5db180dc1343b
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	Xsettings-client-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.2
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility library used by Matchbox utilities.

%description -l pl
Biblioteka narzêdziowa u¿ywana przez narzêdzia Matchbox.

%package devel
Summary:	Header files for Matchbox library
Summary(pl):	Pliki nag³ówkowe biblioteki Matchbox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Xsettings-client-devel
Requires:	libjpeg-devel
Requires:	libpng-devel >= 1.2
Requires:	pango-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel

%description devel
Header files for Matchbox library.

%description devel -l pl
Pliki nag³ówkowe biblioteki Matchbox.

%package static
Summary:	Static Matchbox library
Summary(pl):	Statyczna biblioteka Matchbox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Matchbox library.

%description static -l pl
Statyczna biblioteka Matchbox.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libmb.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmb.so
%{_libdir}/libmb.la
%{_includedir}/libmb
%{_pkgconfigdir}/libmb.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmb.a
