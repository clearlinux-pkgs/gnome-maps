#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-maps
Version  : 3.30.0
Release  : 8
URL      : https://download.gnome.org/sources/gnome-maps/3.30/gnome-maps-3.30.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-maps/3.30/gnome-maps-3.30.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 HPND LGPL-3.0 WTFPL
Requires: gnome-maps-bin
Requires: gnome-maps-lib
Requires: gnome-maps-data
Requires: gnome-maps-license
Requires: gnome-maps-locales
BuildRequires : appstream-glib
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(champlain-0.12)
BuildRequires : pkgconfig(folks)
BuildRequires : pkgconfig(gee-0.8)
BuildRequires : pkgconfig(geoclue-2.0)
BuildRequires : pkgconfig(geocode-glib-1.0)
BuildRequires : pkgconfig(gjs-1.0)
BuildRequires : pkgconfig(rest-0.7)

%description
Maps is a map application for GNOME.
More information on https://wiki.gnome.org/Apps/Maps

%package bin
Summary: bin components for the gnome-maps package.
Group: Binaries
Requires: gnome-maps-data
Requires: gnome-maps-license

%description bin
bin components for the gnome-maps package.


%package data
Summary: data components for the gnome-maps package.
Group: Data

%description data
data components for the gnome-maps package.


%package lib
Summary: lib components for the gnome-maps package.
Group: Libraries
Requires: gnome-maps-data
Requires: gnome-maps-license

%description lib
lib components for the gnome-maps package.


%package license
Summary: license components for the gnome-maps package.
Group: Default

%description license
license components for the gnome-maps package.


%package locales
Summary: locales components for the gnome-maps package.
Group: Default

%description locales
locales components for the gnome-maps package.


%prep
%setup -q -n gnome-maps-3.30.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536145179
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/doc/gnome-maps
cp COPYING %{buildroot}/usr/share/doc/gnome-maps/COPYING
cp src/geojson-vt/LICENSE %{buildroot}/usr/share/doc/gnome-maps/src_geojson-vt_LICENSE
cp src/togeojson/LICENSE %{buildroot}/usr/share/doc/gnome-maps/src_togeojson_LICENSE
cp src/xmldom/LICENSE %{buildroot}/usr/share/doc/gnome-maps/src_xmldom_LICENSE
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gnome-maps

%files
%defattr(-,root,root,-)
/usr/lib64/gnome-maps/girepository-1.0/GnomeMaps-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gnome-maps

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Maps.desktop
/usr/share/dbus-1/services/org.gnome.Maps.service
/usr/share/glib-2.0/schemas/org.gnome.Maps.gschema.xml
/usr/share/gnome-maps/gir-1.0/GnomeMaps-1.0.gir
/usr/share/gnome-maps/icons/hicolor/16x16/apps/layer-not-visible-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/layer-visible-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/layers-button-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/maps-point-end-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/maps-point-end.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/maps-point-start-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/maps-point-start.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-bike-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-button-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-car-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-pedestrian-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-reverse-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-bus-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-cablecar-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-ferry-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-funicular-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-gondolalift-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-subway-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-train-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/16x16/apps/route-transit-tram-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/24x24/apps/user-location-compass.png
/usr/share/gnome-maps/icons/hicolor/24x24/apps/user-location.png
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-continue-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-left-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-right-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-0-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-135-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-180-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-225-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-270-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-315-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-45-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-90-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-roundabout-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-sharpleft-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-sharpright-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-slightleft-symbolic.svg
/usr/share/gnome-maps/icons/hicolor/32x32/apps/maps-direction-slightright-symbolic.svg
/usr/share/gnome-maps/maps-service.json
/usr/share/gnome-maps/org.gnome.Maps
/usr/share/gnome-maps/org.gnome.Maps.data.gresource
/usr/share/gnome-maps/org.gnome.Maps.src.gresource
/usr/share/icons/hicolor/16x16/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/22x22/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/24x24/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/256x256/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/32x32/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/48x48/apps/org.gnome.Maps.png
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Maps-symbolic.svg
/usr/share/metainfo/org.gnome.Maps.appdata.xml

%files lib
%defattr(-,root,root,-)
/usr/lib64/gnome-maps/libgnome-maps.so
/usr/lib64/gnome-maps/libgnome-maps.so.0
/usr/lib64/gnome-maps/libgnome-maps.so.0.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/gnome-maps/COPYING
/usr/share/doc/gnome-maps/src_geojson-vt_LICENSE
/usr/share/doc/gnome-maps/src_togeojson_LICENSE
/usr/share/doc/gnome-maps/src_xmldom_LICENSE

%files locales -f gnome-maps.lang
%defattr(-,root,root,-)

