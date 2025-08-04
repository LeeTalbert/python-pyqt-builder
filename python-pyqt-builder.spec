%define pname pyqt_builder

Name:		python-pyqt-builder
Version:	1.18.2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/%{pname}/%{pname}-%{version}.tar.gz
Summary:	The PyQt build system
URL:		https://pypi.org/project/pyqt-builder/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
The PyQt build system

%files
%{py_sitedir}/pyqtbuild
%{py_sitedir}/pyqt_builder-*.*-info
%{_bindir}/pyqt-bundle
%{_bindir}/pyqt-qt-wheel
