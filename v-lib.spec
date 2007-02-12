Summary:	V-lib - library used by programs written by v13
Summary(pl.UTF-8):	V-lib - biblioteka używana przez programy napisane przez v13
Name:		v-lib
Version:	1.5.3.0
Release:	1
License:	distributable if unchanged (see LICENSE)
Group:		Libraries
Source0:	http://aetos.it.teithe.gr/~v13/vlib/%{name}-%{version}.tar.gz
# Source0-md5:	c63235ffbca3c5208f148fc402ac7795
URL:		http://aetos.it.teithe.gr/~v13/vlib/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V-lib - library used by programs written by v13.

%description -l pl.UTF-8
V-lib - biblioteka używana przez programy napisane przez v13.

%package devel
Summary:	Header files for v-lib
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki v-lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
v-lib development files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki v-lib.

%package static
Summary:	Static v-lib library
Summary(pl.UTF-8):	Statyczna biblioteka v-lib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static v-lib library.

%description static -l pl.UTF-8
Statyczna biblioteka v-lib.

%prep
%setup -q

tail -n +4433 aclocal.m4 > acinclude.m4

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-pcap=linux \
	--enable-ipv6
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes LICENSE TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/v
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
