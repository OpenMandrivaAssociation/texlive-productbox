# revision 20886
# category Package
# catalog-ctan /macros/latex/contrib/gene/productbox
# catalog-date 2010-12-30 01:06:48 +0100
# catalog-license other-free
# catalog-version 1.1
Name:		texlive-productbox
Version:	1.1
Release:	1
Summary:	Typeset a three-dimensional product box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/productbox
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/productbox.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package enables typesetting of a three-dimensional product
box. This product box can be rendered as it is standing on a
surface and some light is shed onto it. Alternatively it can be
typeset as a wireframe to be cut out and glued together. This
will lead to a physical product box. The package requires the
package pgf and TikZ.

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
%{_texmfdistdir}/tex/latex/productbox/productbox.sty
%doc %{_texmfdistdir}/doc/latex/productbox/Makefile
%doc %{_texmfdistdir}/doc/latex/productbox/README
%doc %{_texmfdistdir}/doc/latex/productbox/productbox.bib
%doc %{_texmfdistdir}/doc/latex/productbox/productbox.pdf
#- source
%doc %{_texmfdistdir}/source/latex/productbox/productbox.dtx
%doc %{_texmfdistdir}/source/latex/productbox/productbox.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
