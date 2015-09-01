#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	rb-inotify
Summary:	A Ruby wrapper for Linux's inotify, using FFI
Name:		ruby-%{pkgname}
Version:	0.9.5
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	865ed70ff9f90d5d23dc4ab906358650
URL:		http://github.com/nex3/rb-inotify
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-yard >= 0.4.0
%endif
Requires:	ruby-ffi >= 0.5.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Ruby wrapper for Linux's inotify, using FFI

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md MIT-LICENSE VERSION
%{ruby_vendorlibdir}/rb-inotify.rb
%{ruby_vendorlibdir}/rb-inotify
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
