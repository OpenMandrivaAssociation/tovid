%define name	tovid
%define version	0.31
%define release %mkrel 6

%define title ToVid
%define longtitle Video disc creator

Name: 	 	%{name}
Summary: 	Video disc authoring tools
Version: 	%{version}
Release: 	%{release}

Source:		http://tovid.googlecode.com/files/%{name}-%{version}.tar.gz
# From upstream SVN, re-diffed: allow wx 2.8 as well as 2.6 - AdamW
# 2008/12
Patch0:		tovid-0.31-wx28.patch
# From http://code.google.com/p/tovid/issues/detail?id=20 , can't give
# credit as author's name is obfuscated: fix initial layout of tovidgui
# window with wx 2.8 - AdamW 2008/12
Patch1:		tovid-0.31-frames.patch
URL:		http://tovid.sourceforge.net/
License:	GPLv2+
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	imagemagick
BuildRequires:	python
BuildRequires:	txt2tags
BuildRequires:	desktop-file-utils
Requires:	python
Requires:	wxPythonGTK
Requires:	mplayer mencoder
Requires:	mjpegtools
Requires:	imagemagick
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
%patch0 -p1 -b .wx28
%patch1 -p1 -b .frames

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
