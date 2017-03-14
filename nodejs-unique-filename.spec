%{?scl:%scl_package nodejs-unique-filename}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global packagename unique-filename
%global enable_tests 0

Name:		%{?scl_prefix}nodejs-unique-filename
Version:	1.1.0
Release:	3%{?dist}
Summary:	Generate a unique filename for use in temporary directories or caches

License:	ISC
URL:		https://github.com/iarna/unique-filename.git
Source0:	https://registry.npmjs.org/%{packagename}/-/%{packagename}-%{version}.tgz
Source1:	LICENSE-ISC.txt
# Upstream does not have a license file

Patch0:		nodejs-unique-filename_fix-tests.patch
# the version of npm(tap) in Fedora is *very* old, so we have to patch the
# syntax to fit the old version of tap.  If tap gets updated, we can remove
# this patch.


BuildArch:	noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:	%{?scl_prefix}nodejs-devel
BuildRequires:	%{?scl_prefix}npm(unique-slug)
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(tap)
%endif

%description
Generate a unique filename for use in temporary directories or caches.

%prep
%setup -q -n package
%patch0 -p1
cp -p %{SOURCE1} .

%build
# nothing to do!

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{packagename}
cp -pr package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{packagename}

%nodejs_symlink_deps

#%check
#%nodejs_symlink_deps --check
#%{__nodejs} -e 'require("./")'
#%if 0%{?enable_tests}
#%{_bindir}/tap test
#%else
#%{_bindir}/echo "Tests disabled..."
#%endif

%files
%{!?_licensedir:%global license %doc}
%doc *.md
%license LICENSE-ISC.txt
%{nodejs_sitelib}/%{packagename}

%changelog
* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-3
- Built for RHSCL

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 18 2015 Jared Smith <jsmith@fedoraproject.org> - 1.1.0-1
- Initial packaging
