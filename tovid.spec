%define title ToVid
%define longtitle Video disc creator

Name:		tovid
Summary:	Video disc authoring tools
Version:	0.34
Release:	2

Source:		http://tovid.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://tovid.sourceforge.net/
License:	GPLv2+
Group:		Video
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
Provides:	%{name}-gui = %{version}-%{release}

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
./setup.py install --prefix=%{_prefix} --root=%{buildroot}

rm -f %{buildroot}%{_libdir}/%{name}/.install.log

%files
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/applications/*.desktop
%{py_puresitedir}/libtovid
%{py_puresitedir}/%{name}-%{version}-py*.egg-info
%{_iconsdir}/hicolor/scalable/apps/*.svg
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_iconsdir}/hicolor/*/apps/titleset-wizard.png

