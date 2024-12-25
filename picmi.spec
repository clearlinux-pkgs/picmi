#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : picmi
Version  : 24.12.0
Release  : 76
URL      : https://download.kde.org/stable/release-service/24.12.0/src/picmi-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/picmi-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/picmi-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : qt6base-dev
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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n picmi-24.12.0
cd %{_builddir}/picmi-24.12.0
pushd ..
cp -a picmi-24.12.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735166066
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1735166066
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/picmi
cp %{_builddir}/picmi-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/picmi/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/picmi-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/picmi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/picmi-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/picmi/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/picmi-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/picmi/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
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
/usr/share/picmi/themes/picmi.svgz
/usr/share/qlogging-categories6/picmi.categories
/usr/share/qlogging-categories6/picmi.renamecategories

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
/usr/share/doc/HTML/sl/picmi/index.cache.bz2
/usr/share/doc/HTML/sl/picmi/index.docbook
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
/usr/share/package-licenses/picmi/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f picmi.lang
%defattr(-,root,root,-)

