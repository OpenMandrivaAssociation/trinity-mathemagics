%bcond clang 1

# TDE variables
%define tde_pkg mathemagics
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Summary:		Mathemagics is a RPN Calculator.
Version:		14.1.6
Release:		1
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:		GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/utilities/%{tarball_name}-%{version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DDATA_INSTALL_DIR=%{tde_prefix}/share/apps
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
Mathemagics is a RPN Calculator.


%install -a
%find_lang %{tde_pkg}


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.md
%{tde_prefix}/bin/mathemagics
%{tde_prefix}/share/applications/tde/mathemagics.desktop
%{tde_prefix}/share/apps/mathemagics/
%{tde_prefix}/share/icons/hicolor/22x22/apps/mathemagics.png
%{tde_prefix}/share/icons/hicolor/32x32/apps/mathemagics.png
%{tde_prefix}/share/icons/hicolor/48x48/apps/mathemagics.png
%{tde_prefix}/share/icons/locolor/16x16/apps/mathemagics.png
%{tde_prefix}/share/icons/locolor/32x32/apps/mathemagics.png
%{tde_prefix}/share/doc/tde/HTML/en/mathemagics/
%{tde_prefix}/share/man/man1/mathemagics.1*

