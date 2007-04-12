%define name	tovid
%define version	0.28
%define release %mkrel 2

%define title ToVid
%define longtitle Video disc creator

Name: 	 	%{name}
Summary: 	Video disc authoring tools
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://tovid.sourceforge.net/
License:	GPL
Group:		Video
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
BuildRequires:	python
Requires:	python
Requires:	wxPythonGTK
Requires:	mplayer mencoder
Requires:	mjpegtools
Requires:	ImageMagick
Requires:	ffmpeg
Requires:	dvdauthor
Requires:	vcdimager
Requires:	dvd+rw-tools
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

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}gui" \
		   icon="%{name}.png" \
                   needs="x11"  \
                   title="%{title}" \
                   longtitle="%{longtitle}" \
                   section="Multimedia/Video"\
		   xdg="true"		
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{title}
Comment=%{longtitle}
Exec=%{_bindir}/%{name}gui
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=QT;Video;Player;X-MandrivaLinux-Multimedia-Video;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cp icons/tovid_icon_48.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cp icons/tovid_icon_32.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 icons/tovid_icon_32.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_mandir}/man1/*
%_datadir/applications/mandriva-%{name}.desktop
%{python_sitelib}/libtovid
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png



