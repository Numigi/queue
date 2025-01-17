# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    "name": "Job Queue",
    "version": "13.0.1.0.0",
    "author": "Camptocamp,ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/queue/queue_job",
    "license": "AGPL-3",
    "category": "Generic Modules",
    "depends": ["mail"],
    "external_dependencies": {"python": ["requests"]},
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/queue_job_views.xml",
        "data/queue_data.xml",
    ],
    "installable": True,
    "development_status": "Mature",
    "maintainers": ["guewen"],
}
