Summary:	V-lib.
Name:		v-lib
Version:	1.5.3.0
Release:	1
License:	see LICENSE
Group:		Libraries
Source0:	http://aetos.it.teithe.gr/~v13/vlib/%{name}-%{version}.tar.gz
# Source0-md5:	c63235ffbca3c5208f148fc402ac7795
URL:		http://aetos.it.teithe.gr/~v13/vlib/
BuildRequires:	gcc-c++
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
V-lib.

%package devel
Summary:	Header files and develpment documentation for v-lib
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
v-lib development files.

%package static
Summary:	Static v-lib library
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static v-lib library.

%prep
%setup -q

%build
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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc Changes LICENSE TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/v
%{_aclocaldir}/*.m4
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
