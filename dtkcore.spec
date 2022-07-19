Name:           dtkcore
Version:        5.4.11.2
Release:        1
Summary:        Deepin tool kit core modules
License:        LGPLv3+
URL:            https://github.com/linuxdeepin/dtkcore
%if 0%{?fedora}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{name}_%{version}.orig.tar.xz
%endif
BuildRequires:  gcc-c++
BuildRequires:  annobin
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  gtest-devel

# since f30
Obsoletes:      deepin-tool-kit <= 0.3.3
Obsoletes:      deepin-tool-kit-devel <= 0.3.3
Obsoletes:      dtksettings <= 0.1.7
Obsoletes:      dtksettings-devel <= 0.1.7

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel%{?_isa}

%description devel
Header files and libraries for %{name}.

%prep
%autosetup -p1

%build
# help find (and prefer) qt5 utilities, e.g. qmake, lrelease
export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix} \
           DTK_VERSION=%{version} \
           LIB_INSTALL_DIR=%{_libdir} \
           BIN_INSTALL_DIR=%{_libexecdir}/dtk5 \
           TOOL_INSTALL_DIR=%{_libexecdir}/dtk5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.5*
%dir %{_libexecdir}/dtk5/
%{_libexecdir}/dtk5/dtk-settings
%{_libexecdir}/dtk5/dtk-license.py
%{_libexecdir}/dtk5/dtk-translate.py
%{_libexecdir}/dtk5/deepin-os-release
%{_datadir}/glib-2.0/schemas/*

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_qt5_archdatadir}/mkspecs/features/*.prf
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_libdir}/cmake/Dtk/
%{_libdir}/cmake/DtkCore/
%{_libdir}/cmake/DtkCMake/
%{_libdir}/cmake/DtkTools/
%{_libdir}/pkgconfig/dtkcore.pc
%{_libdir}/lib%{name}.so

%changelog
* Tue Jul 19 2022 konglidong <konglidong@uniontech.com> - 5.4.11.2-1
- Update to 5.4.11.2

* Thu Jul 15 2021 weidong <weidong@uniontech.com> - 5.2.2.3-2
- Format specfile.

* Mon Jul 12 2021 weidong <weidong@uniontech.com> - 5.2.2.3-1
- Update 5.2.2.3

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.2.1-1
- Package init
