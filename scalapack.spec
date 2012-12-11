%define name	scalapack
%define	version	1.8.0
%define release	%mkrel 6
%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %name %{lib_major}

Summary:	Scalapack	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.netlib.org/scalapack/
Source:		http://www.netlib.org/scalapack/scalapack-%{version}.tgz
Patch0: 	scalapack.SLmake.inc.patch
Requires:	blacsmpi-devel >= 1.1
Provides:	%{name}-%{version}
BuildRequires:	gcc-gfortran
BuildRequires:	openmpi

%package        -n %{lib_name}-devel
Summary:	Scalapak 
Group:          Development/Other
Prefix:         %{_prefix}

%description -n %{lib_name}-devel 
The ScaLAPACK (or Scalable LAPACK) library includes a subset of 
LAPACK routines redesigned for distributed memory MIMD parallel
computers. It is currently written in a Single-Program-Multiple-Data 
style using explicit message passing for interprocessor communication. 
It assumes matrices are laid out in a two-dimensional block cyclic 
decomposition.

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset of 
LAPACK routines redesigned for distributed memory MIMD parallel
computers. It is currently written in a Single-Program-Multiple-Data 
style using explicit message passing for interprocessor communication. 
It assumes matrices are laid out in a two-dimensional block cyclic 
decomposition.

%prep
rm -rf %{buildroot}
%setup -q
cp SLmake.inc.example SLmake.inc 
%patch0 -p0
sed -i 's|@SCALAPACK_HOME@|%{_builddir}/%{name}-%{version}|' SLmake.inc

%build
make \
F77=mpif90 \
CC=mpicc \
F77FLAGS="%{optflags} -O3 -fPIC" \
CCFLAGS="%{optflags} -O3 -fPIC"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}/%{name}-%{version}
cp $RPM_BUILD_DIR/%{name}-%{version}/lib%{name}.a %{buildroot}/%{_libdir}/%{name}-%{version}/lib%{name}.a

%clean
rm -fr %{buildroot}

%files -n %{lib_name}-devel
%defattr(-,root,root) 
%attr(644,root,root) %doc README
%{_libdir}/*/lib%{name}.a


%changelog
* Thu Sep 10 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.8.0-6mdv2010.0
+ Revision: 436252
- rebuild
- rebuild
- rebuild

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Pass %%{optflags} to make.
    - Rebuild.

* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.8.0-1mdv2008.1
+ Revision: 168217
- fix no-buildroot-tag
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Wed May 02 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.8.0-1mdv2008.0
+ Revision: 20734
- Removed Packager tag because buildsystem is complaining about it.
- Updated to 1.8.0.
- Fixes made to SLmake patch for this new version.
- Added needed BuildRequires.
- Import scalapack



* Mon May 17 2004 Antoine Ginies <aginies@n2.mandrakesoft.com> 1.7-5mdk
- rebuild
- rpmlint fix

* Tue Aug 6 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.7-4mdk
- build with gcc 3.2

* Wed Jul 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.7-3mdk
- Rebuild

* Tue Jul 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.7-2mdk
- fix install 

* Tue May 28 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.7-1mdk
- first release for Mandrakesoft
