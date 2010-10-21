%define name PyNOAAGeoMagIndiceHandler
%define version 0.0.1r_apha_jedyais
%define unmangled_version 0.0.1r-apha-jedyais
%define release 1

Summary: A python interface to Space NOAA Magnetometer, Solar Wind Electron Proton, Differential Flux and Anisotropy Index from ACE and Stereo A, B satellite.
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{unmangled_version}.tar.gz
License: BSD NEW LICENCE
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: UNKNOWN <UNKNOWN>
Url: http://github.com/priendeau/PyNOAAGeoMagIndiceHandler/blob/master/dist/PyNOAAGeoMagIndiceHandler-0.0.1r-apha-jedyais-apha-jedyais.tar.gz

%description
