/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package com.mycompany.everthinapp1;



/**
 *
 * @author alisa
 */
public class SnakeGame extends javax.swing.JFrame {

    /**
     * Creates new form SnakeGame
     */
    public SnakeGame() {
        initComponents();
    }
    
    
    
    

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">                          
    private void initComponents() {

        Dashboard = new javax.swing.JPanel();
        Score = new javax.swing.JLabel();
        Time = new javax.swing.JLabel();
        ApplesEatedcounterlable = new javax.swing.JLabel();
        GamePanel123 GamePanel123= new GamePanel123();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setTitle("SnakeGame");
        setCursor(new java.awt.Cursor(java.awt.Cursor.DEFAULT_CURSOR));
        setResizable(false);
        setSize(new java.awt.Dimension(1200, 800));
        getContentPane().setLayout(new org.netbeans.lib.awtextra.AbsoluteLayout());

        Dashboard.setBackground(new java.awt.Color(102, 204, 255));

        Score.setText("Score:0");

        Time.setText("Time:00:00");

        ApplesEatedcounterlable.setText("Apples:0");

        javax.swing.GroupLayout DashboardLayout = new javax.swing.GroupLayout(Dashboard);
        Dashboard.setLayout(DashboardLayout);
        DashboardLayout.setHorizontalGroup(
            DashboardLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(DashboardLayout.createSequentialGroup()
                .addGap(31, 31, 31)
                .addComponent(Score)
                .addGap(191, 191, 191)
                .addComponent(ApplesEatedcounterlable)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, 688, Short.MAX_VALUE)
                .addComponent(Time)
                .addGap(151, 151, 151))
        );
        DashboardLayout.setVerticalGroup(
            DashboardLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(DashboardLayout.createSequentialGroup()
                .addGap(34, 34, 34)
                .addGroup(DashboardLayout.createParallelGroup(javax.swing.GroupLayout.Alignment.BASELINE)
                    .addComponent(Score)
                    .addComponent(Time)
                    .addComponent(ApplesEatedcounterlable))
                .addContainerGap(40, Short.MAX_VALUE))
        );

        getContentPane().add(Dashboard, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 0, 1200, -1));
        
        
       

        getContentPane().add(GamePanel123, new org.netbeans.lib.awtextra.AbsoluteConstraints(0, 90, -1, -1));

        pack();

        
    }// </editor-fold>
    
   

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(SnakeGame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(SnakeGame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(SnakeGame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(SnakeGame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        //</editor-fold>
        
        
        

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new SnakeGame().setVisible(true);
            }
        });
    }
    /*@Override
        public void paint(Graphics g){
            g.drawLine(0, 0, 500, 500);
        }
    */

    // Variables declaration - do not modify                     
    private javax.swing.JLabel ApplesEatedcounterlable;
    private javax.swing.JPanel Dashboard;
    private javax.swing.JLabel Score;
    private javax.swing.JLabel Time;
    private javax.swing.JPanel GamePanel123;
    // End of variables declaration                   
}


