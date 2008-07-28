%define name	scalapack
%define	version	1.8.0
%define release	%mkrel 3
%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %name %{lib_major}
#%define lib_name %{lib_name_orig}%{lib_major}

Summary:	Scalapack	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.netlib.org/scalapack/
Source:		http://www.netlib.org/scalapack/scalapack-%{version}.tgz
Patch0: 	scalapack.SLmake.inc.patch
Requires:	blacsmpi-devel >= 1.1
Provides:	%{name}-%{version}
BuildRequires: gcc-gfortran
BuildRequires: openmpi

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
make

%install
mkdir -p %{buildroot}/%{_libdir}/%{name}-%{version}
cp $RPM_BUILD_DIR/%{name}-%{version}/libscalapack.a %{buildroot}/%{_libdir}/%{name}-%{version}/libscalapack.a

%clean
rm -fr %{buildroot}

%files -n %{lib_name}-devel
%defattr(-,root,root) 
%doc README
%{_libdir}/*/libscalapack.a
