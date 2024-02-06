#
# Conditional build:
%bcond_without	zeitgeist	# enable zeitgeist (via libqzeitgeist) supoort

%define		qt6_ver		6.6.1
%define		kfname	kdsoap-ws-discovery-client

Summary:	kdsoap ws discovery client
Name:		kdsoap-ws-discovery-client-qt6
Version:	0.3.0
Release:	1
License:	LGPL v2.1 or LGPL v3
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/kdsoap-ws-discovery-client/kdsoap-ws-discovery-client-%{version}.tar.xz
# Source0-md5:	3696bba16d2c6283704e3f137745a0e8
URL:		http://phonon.kde.org/
BuildRequires:	Qt6Core-devel >= %{qt6_ver}
BuildRequires:	Qt6DBus-devel >= %{qt6_ver}
BuildRequires:	Qt6Designer-devel >= %{qt6_ver}
BuildRequires:	Qt6Gui-devel >= %{qt6_ver}
BuildRequires:	Qt6OpenGL-devel >= %{qt6_ver}
BuildRequires:	Qt6Qml-devel >= %{qt6_ver}
BuildRequires:	Qt6Widgets-devel >= %{qt6_ver}
BuildRequires:	cmake >= 3.20.0
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	kdsoap-qt6-devel >= 2.2.0
BuildRequires:	kf6-extra-cmake-modules >= 5.60
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.21
BuildRequires:	qt6-build >= %{qt6_ver}
BuildRequires:	qt6-build >= %{qt6_ver}
BuildRequires:	qt6-qmake >= %{qt6_ver}
BuildRequires:	qt6-qmake >= %{qt6_ver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	Qt6Core >= %{qt6_ver}
Requires:	Qt6DBus >= %{qt6_ver}
Requires:	Qt6Gui >= %{qt6_ver}
Requires:	Qt6OpenGL >= %{qt6_ver}
Requires:	Qt6Widgets >= %{qt6_ver}
Requires:	kde-common-dirs >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project is trying to create a WS-Discovery client library based on the KDSoap
library. It uses modern C++ 11 and Qt 5.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qt6_ver}
Requires:	Qt6DBus-devel >= %{qt6_ver}
Requires:	Qt6Gui-devel >= %{qt6_ver}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%prep
%setup -q -n kdsoap-ws-discovery-client-%{version}

%build
%cmake -B build \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DQT_MAJOR_VERSION=6

%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%ghost %{_libdir}/libKDSoapWSDiscoveryClient.so.0
%attr(755,root,root) %{_libdir}/libKDSoapWSDiscoveryClient.so.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/KDSoapWSDiscoveryClient
%{_libdir}/cmake/KDSoapWSDiscoveryClient
%{_libdir}/libKDSoapWSDiscoveryClient.so
