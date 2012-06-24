Summary:	MolScript - a tool for producing publication quality molecular images
Summary(pl):	MolScript - narz�dzie do tworzenia obraz�w cz�steczek nadaj�cych si� do publikacji
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

%description -l pl
MolScript jest jednym ze standardowych narz�dzi do tworzenia wysokiej
jako�ci molekularnych obraz�w do p�niejszej publikacji z
tr�jwymiarowych wsp�rz�dnych atom�w. Obrazy mog� zosta� wygenerowane
w formatach: Postscipt (kolorowym lub czarno-bia�ym), Raster3D, VRML,
RGB, JPEG, PNG i GIF. Wyniki mo�na r�wnie� interaktywnie ogl�da� pod
systemem X Window z OpenGL.

Kod �r�d�owy, binarki i dokumentacja nie mog� by� swobodnie
rozpowszechniane, obowi�zuje zastrze�enie. Wymagana jest licencja,
aby uzyska� i u�ywa� program, na szcz�cie nie ma op�at je�li program
u�ywa si� w celach niekomercyjnych. Wersj� licencjonowan� mo�na
otrzyma� pod adresem <http://www.avatar.se/molscript/>.

%prep
%setup -q
%patch0 -p1

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
