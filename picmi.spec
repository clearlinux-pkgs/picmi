#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : picmi
Version  : 23.04.1
Release  : 53
URL      : https://download.kde.org/stable/release-service/23.04.1/src/picmi-23.04.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.1/src/picmi-23.04.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.1/src/picmi-23.04.1.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: picmi-bin = %{version}-%{release}
Requires: picmi-data = %{version}-%{release}
Requires: picmi-license = %{version}-%{release}
Requires: picmi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
PICMI
Project Information
-------------------
Picmi is a number logic game in which cells in a grid have to be colored or
left blank according to numbers given at the side of the grid to reveal a
hidden picture.

%package bin
Summary: bin components for the picmi package.
Group: Binaries
Requires: picmi-data = %{version}-%{release}
Requires: picmi-license = %{version}-%{release}

%description bin
bin components for the picmi package.


%package data
Summary: data components for the picmi package.
Group: Data

%description data
data components for the picmi package.


%package doc
Summary: doc components for the picmi package.
Group: Documentation

%description doc
doc components for the picmi package.


%package license
Summary: license components for the picmi package.
Group: Default

%description license
license components for the picmi package.


%package locales
Summary: locales components for the picmi package.
Group: Default

%description locales
locales components for the picmi package.


%prep
%setup -q -n picmi-23.04.1
cd %{_builddir}/picmi-23.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1684773345
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1684773345
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/picmi
cp %{_builddir}/picmi-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/picmi/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/picmi-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/picmi/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/picmi-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/picmi/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang picmi
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/picmi
/usr/bin/picmi

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.picmi.desktop
/usr/share/icons/hicolor/128x128/apps/picmi.png
/usr/share/icons/hicolor/16x16/apps/picmi.png
/usr/share/icons/hicolor/22x22/apps/picmi.png
/usr/share/icons/hicolor/256x256/apps/picmi.png
/usr/share/icons/hicolor/32x32/apps/picmi.png
/usr/share/icons/hicolor/48x48/apps/picmi.png
/usr/share/icons/hicolor/64x64/apps/picmi.png
/usr/share/metainfo/org.kde.picmi.appdata.xml
/usr/share/picmi/levels/default.xml
/usr/share/picmi/levels/default/antique_phone.xpm
/usr/share/picmi/levels/default/baby_chick.xpm
/usr/share/picmi/levels/default/baby_panda.xpm
/usr/share/picmi/levels/default/basketball.xpm
/usr/share/picmi/levels/default/bass_clef.xpm
/usr/share/picmi/levels/default/bike.xpm
/usr/share/picmi/levels/default/bird.xpm
/usr/share/picmi/levels/default/calculator.xpm
/usr/share/picmi/levels/default/camera.xpm
/usr/share/picmi/levels/default/carlthecat.xpm
/usr/share/picmi/levels/default/clarathecat.xpm
/usr/share/picmi/levels/default/clausthecat.xpm
/usr/share/picmi/levels/default/clef.xpm
/usr/share/picmi/levels/default/clown.xpm
/usr/share/picmi/levels/default/crocodile.xpm
/usr/share/picmi/levels/default/elephant.xpm
/usr/share/picmi/levels/default/halloween.xpm
/usr/share/picmi/levels/default/hourglass.xpm
/usr/share/picmi/levels/default/house.xpm
/usr/share/picmi/levels/default/mobile_phone.xpm
/usr/share/picmi/levels/default/panda.xpm
/usr/share/picmi/levels/default/phone.xpm
/usr/share/picmi/levels/default/picmi.xpm
/usr/share/picmi/levels/default/pirate_dog.xpm
/usr/share/picmi/levels/default/pirate_ship.xpm
/usr/share/picmi/levels/default/policeman.xpm
/usr/share/picmi/levels/default/robot.xpm
/usr/share/picmi/levels/default/santa_claus.xpm
/usr/share/picmi/levels/default/shopping_cart.xpm
/usr/share/picmi/levels/default/soccer.xpm
/usr/share/picmi/levels/default/zebra.xpm
/usr/share/picmi/themes/picmi.desktop
/usr/share/picmi/themes/picmi.png
/usr/share/picmi/themes/picmi.svg
/usr/share/qlogging-categories5/picmi.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/picmi/gameboard.png
/usr/share/doc/HTML/ca/picmi/index.cache.bz2
/usr/share/doc/HTML/ca/picmi/index.docbook
/usr/share/doc/HTML/de/picmi/index.cache.bz2
/usr/share/doc/HTML/de/picmi/index.docbook
/usr/share/doc/HTML/en/picmi/gameboard.png
/usr/share/doc/HTML/en/picmi/index.cache.bz2
/usr/share/doc/HTML/en/picmi/index.docbook
/usr/share/doc/HTML/es/picmi/index.cache.bz2
/usr/share/doc/HTML/es/picmi/index.docbook
/usr/share/doc/HTML/et/picmi/index.cache.bz2
/usr/share/doc/HTML/et/picmi/index.docbook
/usr/share/doc/HTML/fr/picmi/index.cache.bz2
/usr/share/doc/HTML/fr/picmi/index.docbook
/usr/share/doc/HTML/it/picmi/index.cache.bz2
/usr/share/doc/HTML/it/picmi/index.docbook
/usr/share/doc/HTML/nl/picmi/index.cache.bz2
/usr/share/doc/HTML/nl/picmi/index.docbook
/usr/share/doc/HTML/pt/picmi/index.cache.bz2
/usr/share/doc/HTML/pt/picmi/index.docbook
/usr/share/doc/HTML/pt_BR/picmi/index.cache.bz2
/usr/share/doc/HTML/pt_BR/picmi/index.docbook
/usr/share/doc/HTML/sv/picmi/index.cache.bz2
/usr/share/doc/HTML/sv/picmi/index.docbook
/usr/share/doc/HTML/uk/picmi/gameboard.png
/usr/share/doc/HTML/uk/picmi/index.cache.bz2
/usr/share/doc/HTML/uk/picmi/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/picmi/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/picmi/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/picmi/7697008f58568e61e7598e796eafc2a997503fde

%files locales -f picmi.lang
%defattr(-,root,root,-)

