Name:           zrythm
Version:        0.8.604
Release:        1%{?dist}
Summary:        Digital Audio Workstation

License:        AGPLv3+
URL:            https://www.zrythm.org
Source0:        https://www.zrythm.org/releases/zrythm-%{version}.tar.xz

BuildRequires:  meson >= 0.53.0
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  xdg-utils
BuildRequires:  help2man
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  git
BuildRequires:  graphviz-devel
BuildRequires:  python3-sphinx
BuildRequires:  pandoc
BuildRequires:  texi2html
BuildRequires:  lilv-devel
BuildRequires:  libcyaml-devel
BuildRequires:  libaudec-devel
BuildRequires:  gtk3-devel
BuildRequires:  fftw-devel
BuildRequires:  gtksourceview3-devel
BuildRequires:  guile22-devel
BuildRequires:  libzstd-devel
BuildRequires:  rubberband-devel
BuildRequires:  libyaml-devel
BuildRequires:  libgtop2-devel

%description
Zrythm is a digital audio workstation designed to be featureful and easy to
use. It allows limitless automation through curves, LFOs and envelopes,
supports multiple plugin formats including LV2, VST2 and VST3, works with
multiple backends including JACK, RtAudio/RtMidi and SDL2, assists with chord
progressions via a special Chord Track and chord pads, and can be used in
multiple languages including English, French, Portuguese, Japanese and German.

%prep
%autosetup

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_bindir}/zrythm
%{_bindir}/zrythm_launch
%{_datadir}/applications/zrythm.desktop
%{_sysconfdir}/bash_completion.d/zrythm
%{_datadir}/fonts/zrythm/DSEG14-Classic-MINI/*
%{_datadir}/glib-2.0/schemas/org.zrythm.Zrythm.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/zrythm.svg
%{_datadir}/locale/*/LC_MESSAGES/zrythm.mo
%{_mandir}/man1/zrythm.1.gz
%{_datadir}/mime/packages/org.zrythm.Zrythm-mime.xml
%{_datadir}/zrythm/samples/square_emphasis.wav
%{_datadir}/zrythm/samples/square_normal.wav
%{_datadir}/zrythm/sourceview-styles/monokai-extended-zrythm.xml
%{_datadir}/zrythm/themes/icons/zrythm-dark/*
%{_datadir}/zrythm/themes/zrythm-theme.css

%changelog
* Sun Jul 05 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.8.604-1
- Update to 0.8.604

* Mon Jun  8 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.8.459-1
- Initial build
