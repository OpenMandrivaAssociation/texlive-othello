%global tl_name othello
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Modification of a Go package to create othello boards
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/othello
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/othello.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package (based on Kolodziejska's go), and fonts (as Metafont source)
are provided.

