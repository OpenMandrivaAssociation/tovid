%define name	tovid
%define version	0.31
%define release %mkrel 4

%define title ToVid
%define longtitle Video disc creator

Name: 	 	%{name}
Summary: 	Video disc authoring tools
Version: 	%{version}
Release: 	%{release}

Source:		http://tovid.googlecode.com/files/%{name}-%{version}.tar.gz
# Official upstream patches for various bugs: http://www.createphpbb.com/tovid/viewtopic.php?t=242
URL:		http://tovid.sourceforge.net/
License:	GPLv2+
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
# for todiscgui, bug #31895
Requires:	tkinter
BuildArch:	noarch
Provides:	%name-gui

%description
Tovid is a collection of video disc authoring tools; it can help you create
your own DVDs, VCDs, and SVCDs for playback on your home DVD player.

Note: Some features will be unavailable unless you also install the
      transcode package, available elsewhere.

%prep
%setup -q

%build
%configure2_5x

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

perl -pi -e 's,tovid.svg,tovid,g' $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%if %mdkversion < 200900
%post
%update_menus
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_icon_cache hicolor
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{py_puresitedir}/libtovid
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/*/apps/%name.png
