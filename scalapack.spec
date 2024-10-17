%define old_lib_major 1
%define old_lib_name %mklibname %{name} %{old_lib_major}
%define old_lib_devel %{old_lib_name}-devel

Summary: A subset of LAPACK routines redesigned for heterogeneous computing
Name: scalapack
Version: 1.7.5
Release: 21%{?dist}
# This is freely distributable without any restrictions.
License: Public Domain

URL: https://www.netlib.org/lapack-dev/
Source0: http://www.netlib.org/scalapack/scalapack-%{version}.tgz
Source1: %{name}.rpmlintrc
BuildRequires: lapack-devel, blas-devel
BuildRequires: gcc-gfortran, glibc-devel
BuildRequires: blacs-mpich-devel, mpich-devel-static
BuildRequires: blacs-openmpi-devel, openmpi-devel

Patch0: scalapack-1.7-fedora.patch

%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset 
of LAPACK routines redesigned for distributed memory MIMD 
parallel computers. It is currently written in a 
Single-Program-Multiple-Data style using explicit message 
passing for inter-processor communication. It assumes 
matrices are laid out in a two-dimensional block cyclic 
decomposition.

ScaLAPACK is designed for heterogeneous computing and is 
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on 
block-partitioned algorithms in order to minimize the frequency 
of data movement between different levels of the memory hierarchy. 
(For such machines, the memory hierarchy includes the off-processor 
memory of other processors, in addition to the hierarchy of registers, 
cache, and local memory on each processor.) The fundamental building 
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) 
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra 
Communication Subprograms (BLACS) for communication tasks that arise 
frequently in parallel linear algebra computations. In the ScaLAPACK 
routines, all inter-processor communication occurs within the PBLAS and the 
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK 
routines resemble their LAPACK equivalents as much as possible. 

%package common
Summary: Common files for scalapack
%rename %{old_lib_devel}

%description common
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains common files which are not specific
to any MPI implementation.

%package mpich
Summary: ScaLAPACK libraries compiled against mpich

Requires: %{name}-common = %{version}-%{release}
# For dir ownership
Requires: mpich

Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 1.7.5-19
# This is a lie, but something needs to obsolete it.
Provides: %{name}-lam = %{version}-%{release}
Obsoletes: %{name}-lam <= 1.7.5-7

%description mpich
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK libraries compiled with mpich.

%package mpich-devel
Summary: Development libraries for ScaLAPACK (mpich)

Requires: %{name}-mpich = %{version}-%{release}
Provides: %{name}-lam-devel = %{version}-%{release}
Obsoletes: %{name}-lam-devel <= 1.7.5-7
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 1.7.5-19

%description mpich-devel
This package contains development libraries for ScaLAPACK, compiled
against mpich.

%package mpich-static
Summary: Static libraries for ScaLAPACK (mpich)

Provides: %{name}-lam-static = %{version}-%{release}
Obsoletes: %{name}-lam-static <= 1.7.5-7
Requires: %{name}-mpich-devel = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 1.7.5-19

%description mpich-static
This package contains static libraries for ScaLAPACK, compiled
against mpich.

%package openmpi
Summary: ScaLAPACK libraries compiled against openmpi

Requires: %{name}-common = %{version}-%{release}
# For dir ownership
Requires: openmpi

%description openmpi
The ScaLAPACK (or Scalable LAPACK) library includes a subset
of LAPACK routines redesigned for distributed memory MIMD
parallel computers. It is currently written in a
Single-Program-Multiple-Data style using explicit message
passing for inter-processor communication. It assumes
matrices are laid out in a two-dimensional block cyclic
decomposition.

ScaLAPACK is designed for heterogeneous computing and is
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on
block-partitioned algorithms in order to minimize the frequency
of data movement between different levels of the memory hierarchy.
(For such machines, the memory hierarchy includes the off-processor
memory of other processors, in addition to the hierarchy of registers,
cache, and local memory on each processor.) The fundamental building
blocks of the ScaLAPACK library are distributed memory versions (PBLAS)
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra
Communication Subprograms (BLACS) for communication tasks that arise
frequently in parallel linear algebra computations. In the ScaLAPACK
routines, all inter-processor communication occurs within the PBLAS and the
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK
routines resemble their LAPACK equivalents as much as possible.

This package contains ScaLAPACK libraries compiled with openmpi.

%package openmpi-devel
Summary: Development libraries for ScaLAPACK (openmpi)

Requires: %{name}-openmpi = %{version}-%{release}

%description openmpi-devel
This package contains development libraries for ScaLAPACK, compiled
against openmpi.

%package openmpi-static
Summary: Static libraries for ScaLAPACK (openmpi)

Requires: %{name}-openmpi-devel = %{version}-%{release}

%description openmpi-static
This package contains static libraries for ScaLAPACK, compiled
against openmpi.

%prep
%setup -q -c -n %{name}-%{version}
find . -type f | xargs chmod a+r
%patch0 -p1
cd %{name}-%{version}/
sed -i 's!BLACSdir      =.*!BLACSdir      = %{_libdir}!' SLmake.inc
cd ..
for i in mpich openmpi; do
  cp -a %{name}-%{version} %{name}-%{version}-$i
  sed -i "s|FOO|$i|g" %{name}-%{version}-$i/SLmake.inc
done

%build
%define dobuild() \
cd %{name}-%{version}-$MPI_COMPILER_NAME ; \
make lib ; \
cd ..

# Build mpich version
export MPI_COMPILER_NAME=mpich
%{_mpich_load}
RPM_OPT_FLAGS=`echo $CFLAGS`
%dobuild
%{_mpich_unload}

# Build OpenMPI version
export MPI_COMPILER_NAME=openmpi
%{_openmpi_load}
RPM_OPT_FLAGS=`echo $CFLAGS`
%dobuild
%{_openmpi_unload}

%install
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}

for i in mpich openmpi; do
  mkdir -p %{buildroot}%{_libdir}/$i/lib/
  pushd %{name}-%{version}-$i
  for f in *.a *.so*; do
    cp -f $f %{buildroot}%{_libdir}/$i/lib/$f
  done
  popd
  pushd %{buildroot}%{_libdir}/$i/lib/
  ln -fs libscalapack.so.1.0.0 libscalapack.so.1
  ln -s libscalapack.so.1.0.0 libscalapack.so
  popd
done

# Copy docs
cd %{name}-%{version}
cp -f INSTALL/scalapack_install.ps ../
cp -f README ../

#cp -f TESTING/x* ${RPM_BUILD_ROOT}%{_bindir}

%files common
%doc scalapack_install.ps README
# %{_bindir}/x*

%files mpich
%{_libdir}/mpich/lib/libscalapack.so.*

%files mpich-devel
%{_libdir}/mpich/lib/libscalapack.so

%files mpich-static
%{_libdir}/mpich/lib/libscalapack.a

%files openmpi
%{_libdir}/openmpi/lib/libscalapack.so.*

%files openmpi-devel
%{_libdir}/openmpi/lib/libscalapack.so

%files openmpi-static
%{_libdir}/openmpi/lib/libscalapack.a
