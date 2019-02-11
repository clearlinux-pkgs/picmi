#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : picmi
Version  : 18.12.2
Release  : 2
URL      : https://download.kde.org/stable/applications/18.12.2/src/picmi-18.12.2.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.2/src/picmi-18.12.2.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.2/src/picmi-18.12.2.tar.xz.sig
Summary  : A nonogram logic game for KDE
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: picmi-bin = %{version}-%{release}
Requires: picmi-data = %{version}-%{release}
Requires: picmi-license = %{version}-%{release}
Requires: picmi-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n picmi-18.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549910195
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549910195
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/picmi
cp COPYING %{buildroot}/usr/share/package-licenses/picmi/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/picmi/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang picmi

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/kxmlgui5/picmi/picmiui.rc
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
/usr/share/picmi/levels/default/mobile_phone.xpm
/usr/share/picmi/levels/default/panda.xpm
/usr/share/picmi/levels/default/phone.xpm
/usr/share/picmi/levels/default/picmi.xpm
/usr/share/picmi/levels/default/pirate_dog.xpm
/usr/share/picmi/levels/default/policeman.xpm
/usr/share/picmi/levels/default/robot.xpm
/usr/share/picmi/levels/default/santa_claus.xpm
/usr/share/picmi/levels/default/shopping_cart.xpm
/usr/share/picmi/levels/default/soccer.xpm
/usr/share/picmi/levels/default/zebra.xpm
/usr/share/picmi/themes/picmi.desktop
/usr/share/picmi/themes/picmi.png
/usr/share/picmi/themes/picmi.svg

%files doc
%defattr(0644,root,root,0755)
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
/usr/share/package-licenses/picmi/COPYING
/usr/share/package-licenses/picmi/COPYING.DOC

%files locales -f picmi.lang
%defattr(-,root,root,-)
