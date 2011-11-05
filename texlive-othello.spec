# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/othello
# catalog-date 2007-01-12 15:52:44 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-othello
Version:	20070112
Release:	1
Summary:	Create othello boards in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/othello
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package (based on Kolodziejska's go), and fonts (as MetaFont
source) are provided.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
