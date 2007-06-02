%define name	tovid
%define version	0.30
%define release %mkrel 3

%define title ToVid
%define longtitle Video disc creator

Name: 	 	%{name}
Summary: 	Video disc authoring tools
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
# Official upstream patches for various bugs: http://www.createphpbb.com/tovid/viewtopic.php?t=242
Patch0:		todiscgui.diff
Patch1:		tovid-0.30.2.patch
URL:		http://tovid.sourceforge.net/
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	python
BuildRequires:	txt2tags
BuildRequires:	desktop-file-utils
Requires:	python
Requires:	wxPythonGTK
Requires:	wxpython2.6
Requires:	mplayer mencoder
Requires:	mjpegtools
Requires:	ImageMagick
Requires:	ffmpeg
Requires:	dvdauthor
Requires:	vcdimager
Requires:	dvd+rw-tools
Requires:	cdrdao
BuildArch:	noarch
Provides:	%name-gui

%description
Tovid is a collection of video disc authoring tools; it can help you create
your own DVDs, VCDs, and SVCDs for playback on your home DVD player.

Note: Some features will be unavailable unless you also install the
      transcode package, available elsewhere.

%prep
%setup -q
%patch0 -p0 -b .hidden
%patch1 -p1 -b .ffmpeg

%build
# The upstream build incorrectly uses pyexecdir instead of pythondir.
# This will result in installation to /usr/lib64 on an x86-64 machine.
# The app contains only pure python files, so should install to /usr/lib
# on all archs. To achieve this, we replace pyexecdir with pythondir in
# Makefile.am and re-generate the Makefile.
perl -pi -e 's,pyexec,python,g' Makefile.am
aclocal
automake
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp icons/tovid_icon_48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp icons/tovid_icon_32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/tovid_icon_32.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

mv $RPM_BUILD_ROOT/%_iconsdir/hicolor/128x128/apps/%{name}_icon_128.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/128x128/apps/%name.png
mv $RPM_BUILD_ROOT/%_iconsdir/hicolor/64x64/apps/%{name}_icon_64.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/64x64/apps/%name.png
mv $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%{name}_icon_48.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/48x48/apps/%name.png
mv $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%{name}_icon_32.png $RPM_BUILD_ROOT/%_iconsdir/hicolor/32x32/apps/%name.png

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

perl -pi -e 's,tovid.svg,tovid,g' $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%post
%update_menus
%update_icon_cache hicolor

%postun
%clean_menus
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{py_puresitedir}/libtovid
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/128x128/apps/%name.png
%{_iconsdir}/hicolor/64x64/apps/%name.png
%{_iconsdir}/hicolor/48x48/apps/%name.png
%{_iconsdir}/hicolor/32x32/apps/%name.png
