%define name	tovid
%define version	0.34
%define release %mkrel 1

%define title ToVid
%define longtitle Video disc creator

Name: 	 	%{name}
Summary: 	Video disc authoring tools
Version: 	%{version}
Release: 	%{release}

Source:		http://tovid.googlecode.com/files/%{name}-%{version}.tar.gz
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
Requires:	tix
# for todiscgui, bug #31895
Requires:	tkinter
BuildArch:	noarch
Provides:	%{name}-gui

%description
Tovid is a collection of video disc authoring tools; it can help you create
your own DVDs, VCDs, and SVCDs for playback on your home DVD player.

Note: Some features will be unavailable unless you also install the
      transcode package, available elsewhere.

%prep
%setup -q

%build
./setup.py build

%install
rm -rf %{buildroot}
./setup.py install --prefix=%{_prefix} --root=%{buildroot}

rm -f %{buildroot}%{_libdir}/%{name}/.install.log

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
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{py_puresitedir}/libtovid
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/titleset-wizard.png
