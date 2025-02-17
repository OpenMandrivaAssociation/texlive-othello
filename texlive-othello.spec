Name:		texlive-othello
Version:	15878
Release:	2
Summary:	Modification of a Go package to create othello boards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/othello
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package (based on Kolodziejska's go), and fonts (as Metafont
source) are provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/othello/ot.mf
%{_texmfdistdir}/fonts/source/public/othello/ot10.mf
%{_texmfdistdir}/fonts/source/public/othello/ot15.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1bla10.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1bla15.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1bla20.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1black.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1neu.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1neu10.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1neu15.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1neu20.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1whi10.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1whi15.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1whi20.mf
%{_texmfdistdir}/fonts/source/public/othello/ot1white.mf
%{_texmfdistdir}/fonts/tfm/public/othello/ot10.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot15.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1bla10.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1bla15.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1bla20.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1neu10.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1neu15.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1neu20.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1whi10.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1whi15.tfm
%{_texmfdistdir}/fonts/tfm/public/othello/ot1whi20.tfm
%{_texmfdistdir}/tex/latex/othello/othello.sty
%doc %{_texmfdistdir}/doc/latex/othello/boards.tex
%doc %{_texmfdistdir}/doc/latex/othello/ot.bat
%doc %{_texmfdistdir}/doc/latex/othello/ot1.bat.bat
%doc %{_texmfdistdir}/doc/latex/othello/othello.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
