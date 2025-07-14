Summary:	MolScript - a tool for producing publication quality molecular images
Summary(pl.UTF-8):	MolScript - narzędzie do tworzenia obrazów cząsteczek nadających się do publikacji
Name:		molscript
Version:	2.1.2
Release:	1
License:	*NOT DISTRIBUTABLE* (c) 1997-1998 Per Kraulis
Group:		Applications/Science
Source0:	%{name}-%{version}.tar.gz
URL:		http://www.avatar.se/molscript/
Patch0:		%{name}-%{version}.patch
NoSource:	0
BuildRequires:	gd-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MolScript is one of the standard tools used for producing publication
quality molecular graphics images from 3D atomic coordinates,
particularly protein structures. The images can be produced in
Postscript (colour or black and white), Raster3D, VRML, RGB, JPEG, PNG
and GIF formats. The output can also be viewed interactively using X
windows with OpenGL. The software allows the representation of protein
secondary structure, alpha-helices and beta-strands, as smooth helical
ribbons or cylinders and smooth directional arrows respectively.

The MolScript source code, binaries and documentation cannot be
distributed freely as it is copyrighted 1997-1998 Per Kraulis. A
license is required to obtain and use the program, fortunately there
is no fee for academic institutions that use MolScript exclusively for
academic work. The licensed distribution package is available from
<http://www.avatar.se/molscript/>.

%description -l pl.UTF-8
MolScript jest jednym ze standardowych narzędzi do tworzenia wysokiej
jakości molekularnych obrazów do późniejszej publikacji z
trójwymiarowych współrzędnych atomów. Obrazy mogą zostać wygenerowane
w formatach: Postscipt (kolorowym lub czarno-białym), Raster3D, VRML,
RGB, JPEG, PNG i GIF. Wyniki można również interaktywnie oglądać pod
systemem X Window z OpenGL.

Kod źródłowy, binarki i dokumentacja nie mogą być swobodnie
rozpowszechniane, obowiązuje zastrzeżenie. Wymagana jest licencja,
aby uzyskać i używać program, na szczęście nie ma opłat jeśli program
używa się w celach niekomercyjnych. Wersję licencjonowaną można
otrzymać pod adresem <http://www.avatar.se/molscript/>.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	COPT="%{rpmcflags}"
#cd examples
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install molauto molscript $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DISCLAIMER doc examples
%attr(755,root,root) %{_bindir}/molauto
%attr(755,root,root) %{_bindir}/molscript
