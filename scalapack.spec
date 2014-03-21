%define lib_name_orig lib%{name}
%define lib_major 1
%define lib_name %mklibname %{name} %{lib_major}

%define debug_package %{nil}

Summary:	Scalapack
Name:		scalapack
Version:	2.0.2
Release:	1
License:	GPL
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.netlib.org/scalapack/
Source:		http://www.netlib.org/scalapack/scalapack-%{version}.tgz
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
%setup -q
cp SLmake.inc.example SLmake.inc
# %patch0 -p0
sed -i 's|@SCALAPACK_HOME@|%{_builddir}/%{name}-%{version}|' SLmake.inc

%build
make \
F77=mpif90 \
CC=mpicc \
F77FLAGS="%{optflags} -O3 -fPIC" \
CCFLAGS="%{optflags} -O3 -fPIC"

%install
mkdir -p %{buildroot}/%{_libdir}/%{name}-%{version}
# cp %{buildroot}/%{name}-%{version}/lib%{name}.a %{buildroot}/%{_libdir}/%{name}-%{version}/lib%{name}.a

%files -n %{lib_name}-devel
%attr(644,root,root) %doc README
# %{_libdir}/*/lib%{name}.a

