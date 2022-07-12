#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kscreen
Version  : 5.25.3
Release  : 68
URL      : https://download.kde.org/stable/plasma/5.25.3/kscreen-5.25.3.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.25.3/kscreen-5.25.3.tar.xz
Source1  : https://download.kde.org/stable/plasma/5.25.3/kscreen-5.25.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 LGPL-2.1
Requires: kscreen-bin = %{version}-%{release}
Requires: kscreen-data = %{version}-%{release}
Requires: kscreen-lib = %{version}-%{release}
Requires: kscreen-license = %{version}-%{release}
Requires: kscreen-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(x11-xcb)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libkscreen-dev
BuildRequires : qtbase-dev mesa-dev

%description
This file describes everything that the Daemon does or should do.
This daemon will restore and save screen configurations depending on which monitors are connected.
In case not known configuration is saved, a new one will be created following some principles.

%package bin
Summary: bin components for the kscreen package.
Group: Binaries
Requires: kscreen-data = %{version}-%{release}
Requires: kscreen-license = %{version}-%{release}

%description bin
bin components for the kscreen package.


%package data
Summary: data components for the kscreen package.
Group: Data

%description data
data components for the kscreen package.


%package lib
Summary: lib components for the kscreen package.
Group: Libraries
Requires: kscreen-data = %{version}-%{release}
Requires: kscreen-license = %{version}-%{release}

%description lib
lib components for the kscreen package.


%package license
Summary: license components for the kscreen package.
Group: Default

%description license
license components for the kscreen package.


%package locales
Summary: locales components for the kscreen package.
Group: Default

%description locales
locales components for the kscreen package.


%prep
%setup -q -n kscreen-5.25.3
cd %{_builddir}/kscreen-5.25.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657634954
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657634954
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kscreen
cp %{_builddir}/kscreen-5.25.3/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/kscreen-5.25.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/kscreen-5.25.3/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kscreen/2123756e0b1fc8243547235a33c0fcabfe3b9a51
cp %{_builddir}/kscreen-5.25.3/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kscreen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
cp %{_builddir}/kscreen-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kscreen/7d9831e05094ce723947d729c2a46a09d6e90275
cp %{_builddir}/kscreen-5.25.3/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/kscreen/7d9831e05094ce723947d729c2a46a09d6e90275
pushd clr-build
%make_install
popd
%find_lang kcm_kscreen
%find_lang kscreen
%find_lang plasma_applet_org.kde.kscreen

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kscreen-console

%files data
%defattr(-,root,root,-)
/usr/share/kded_kscreen/qml/OsdSelector.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/Orientation.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/Output.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/OutputIdentifier.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/OutputPanel.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/Panel.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/RotationButton.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/Screen.qml
/usr/share/kpackage/kcms/kcm_kscreen/contents/ui/main.qml
/usr/share/kservices5/kcm_kscreen.desktop
/usr/share/kservices5/plasma-applet-org.kde.kscreen.desktop
/usr/share/metainfo/org.kde.kscreen.appdata.xml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/InhibitionHint.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/PresentationModeItem.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/ScreenLayoutSelection.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.kscreen/metadata.json
/usr/share/qlogging-categories5/kscreen.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcms/kcm_kscreen.so
/usr/lib64/qt5/plugins/kf5/kded/kscreen.so
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_kscreen.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kscreen/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/kscreen/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kscreen/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/kscreen/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567

%files locales -f kcm_kscreen.lang -f kscreen.lang -f plasma_applet_org.kde.kscreen.lang
%defattr(-,root,root,-)

