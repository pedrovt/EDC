<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <section>
            <h2>Courses</h2>
            <table>
                <tr>
                    <th align="left">Course ID</th>
                    <th align="left">Course Name</th>
                </tr>
                <xsl:for-each select="cursos/curso">
                    <tr>
                        <td><xsl:value-of select="guid"/></td>
                        <td><xsl:value-of select="nome"/></td>
                    </tr>
                </xsl:for-each>
            </table>
        </section>
    </xsl:template>

</xsl:stylesheet>