Summary:	Utility library used by Matchbox utilities
Summary(pl.UTF-8):	Biblioteka narzędziowa używana przez narzędzia Matchbox
Name:		libmatchbox
Version:	1.9
Release:	10
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://projects.o-hand.com/matchbox/sources/libmatchbox/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	9f73e7515cc4679171a5db180dc1343b
Patch0:		%{name}-ac.patch
Patch1:		%{name}-libpng15.patch
Patch2:		%{name}-libs.patch
URL:		http://projects.o-hand.com/matchbox/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel >= 1.4
BuildRequires:	libtool
BuildRequires:	libxsettings-client-devel
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utility library used by Matchbox utilities.

%description -l pl.UTF-8
Biblioteka narzędziowa używana przez narzędzia Matchbox.

%package devel
Summary:	Header files for Matchbox library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Matchbox
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libjpeg-devel
Requires:	libpng-devel >= 1.2
Requires:	libxsettings-client-devel
Requires:	pango-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXft-devel

%description devel
Header files for Matchbox library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Matchbox.

%package static
Summary:	Static Matchbox library
Summary(pl.UTF-8):	Statyczna biblioteka Matchbox
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Matchbox library.

%description static -l pl.UTF-8
Statyczna biblioteka Matchbox.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's/png_check_sig( header, 8 )/!png_sig_cmp(header, 0, 8)/g' libmb/mbpixbuf.c

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-jpeg \
	--enable-pango \
	--enable-xsettings
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
