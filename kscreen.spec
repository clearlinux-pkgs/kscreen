#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : kscreen
Version  : 5.15.5
Release  : 18
URL      : https://download.kde.org/stable/plasma/5.15.5/kscreen-5.15.5.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.15.5/kscreen-5.15.5.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.15.5/kscreen-5.15.5.tar.xz.sig
Summary  : KDE's screen management software
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: kscreen-bin = %{version}-%{release}
Requires: kscreen-data = %{version}-%{release}
Requires: kscreen-lib = %{version}-%{release}
Requires: kscreen-license = %{version}-%{release}
Requires: kscreen-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : kglobalaccel-dev
BuildRequires : libkscreen-dev
BuildRequires : plasma-framework-dev
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
%setup -q -n kscreen-5.15.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557241499
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557241499
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kscreen
cp COPYING %{buildroot}/usr/share/package-licenses/kscreen/COPYING
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/kscreen/COPYING.LGPL
pushd clr-build
%make_install
popd
%find_lang kcm_displayconfiguration
%find_lang kscreen
%find_lang plasma_applet_org.kde.kscreen

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kscreen-console

%files data
%defattr(-,root,root,-)
/usr/share/icons/hicolor/48x48/actions/kdocumentinfo.png
/usr/share/icons/hicolor/scalable/actions/kdocumentinfo.svgz
/usr/share/kcm_kscreen/qml/Output.qml
/usr/share/kcm_kscreen/qml/OutputIdentifier.qml
/usr/share/kcm_kscreen/qml/Tip.qml
/usr/share/kcm_kscreen/qml/main.qml
/usr/share/kded_kscreen/qml/Osd.qml
/usr/share/kded_kscreen/qml/OsdItem.qml
/usr/share/kded_kscreen/qml/OsdSelector.qml
/usr/share/kded_kscreen/qml/OutputIdentifier.qml
/usr/share/kservices5/kcm_kscreen.desktop
/usr/share/kservices5/plasma-applet-org.kde.kscreen.desktop
/usr/share/metainfo/org.kde.kscreen.appdata.xml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/PresentationModeItem.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/ScreenLayoutSelection.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/contents/ui/main.qml
/usr/share/plasma/plasmoids/org.kde.kscreen/metadata.desktop
/usr/share/plasma/plasmoids/org.kde.kscreen/metadata.json
/usr/share/xdg/kscreen.categories

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kcm_kscreen.so
/usr/lib64/qt5/plugins/kf5/kded/kscreen.so
/usr/lib64/qt5/plugins/plasma/applets/plasma_applet_kscreen.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kscreen/COPYING
/usr/share/package-licenses/kscreen/COPYING.LGPL

%files locales -f kcm_displayconfiguration.lang -f kscreen.lang -f plasma_applet_org.kde.kscreen.lang
%defattr(-,root,root,-)

